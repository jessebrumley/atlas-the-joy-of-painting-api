from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'bob_ross_paintings'
}

@app.route('/episodes', methods=['GET'])
def get_episodes():
    # Establish a new database connection for the request
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        # Get query parameters
        month = request.args.get('month')  # e.g., '1' for January
        subjects = request.args.get('subject')  # e.g., 'mountain,lake'
        colors = request.args.get('color')  # e.g., 'blue,green'

        # Start building the SQL query
        query = """
            SELECT DISTINCT episodes.episode_id, episodes.episode, episodes.title, episodes.date
            FROM episodes
            JOIN paintings ON episodes.episode_id = paintings.episode
            JOIN painting_colors ON paintings.painting_id = painting_colors.painting_id
            JOIN colors ON painting_colors.color_id = colors.color_id
            JOIN episode_subjects ON episodes.episode_id = episode_subjects.episode_id
            JOIN subjects ON episode_subjects.subject_id = subjects.subject_id
        """
        params = []

        # Add subject filtering if requested
        if subjects:
            subject_list = subjects.split(",")  # Split subjects into a list
            placeholders = ", ".join(["%s"] * len(subject_list))
            query += """
                WHERE subjects.subject_name IN ({})
            """.format(placeholders)
            params.extend(subject_list)

        # Add color filtering if requested
        if colors:
            color_list = colors.split(",")  # Split colors into a list
            color_placeholders = ", ".join(["%s"] * len(color_list))
            if "WHERE" not in query:
                query += " WHERE"
            else:
                query += " AND"
            query += """
                colors.color_name IN ({})
            """.format(color_placeholders)
            params.extend(color_list)

        # Add month filtering if requested
        if month:
            if "WHERE" not in query:
                query += " WHERE"
            else:
                query += " AND"
            query += " MONTH(episodes.date) = %s"
            params.append(month)

        query += " ORDER BY episodes.date"

        # Execute the query
        cursor.execute(query, params)
        results = cursor.fetchall()

        # Format the results as JSON
        episodes = [
            {
                "episode_id": row[0],
                "episode": row[1],
                "title": row[2],
                "date": row[3]
            }
            for row in results
        ]
        return jsonify(episodes)
    finally:
        # Close the database connection
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
