from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'bob_ross_paintings'
}

# Mapping month names to their numeric equivalents
month_name_to_number = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
}

@app.route('/episodes', methods=['GET'])
def get_episodes():
    conn = None
    cursor = None
    try:
        # Establish a new database connection for the request
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        if not conn.is_connected():
            return jsonify({"error": "Unable to connect to the database"}), 500

        # Get query parameters
        month = request.args.get('month')  # e.g., '1' for January or 'January'
        subjects = request.args.get('subject')  # e.g., 'mountain,lake'
        colors = request.args.get('color')  # e.g., 'black_gesso,bright_red'
        filter_type = request.args.get('filter_type', 'all')  # 'all' or 'any'

        # Validate 'month' parameter
        if month:
            try:
                # Check if the month is a numeric value
                month = int(month)
                if month < 1 or month > 12:
                    return jsonify({"error": "Invalid month. Please provide a value between 1 and 12."}), 400
            except ValueError:
                # If not numeric, check if it's a valid month name
                month = month.strip().lower()
                if month not in month_name_to_number:
                    return jsonify({"error": f"Invalid month name. Please provide a valid month name (e.g., January, February)."}), 400
                month = month_name_to_number[month]

        # Validate 'color' parameter
        if colors:
            color_list = colors.split(",")
            if not all(isinstance(c, str) and c.strip() != '' for c in color_list):
                return jsonify({"error": "Invalid color input. Please provide valid color names."}), 400

        # Validate 'subject' parameter
        if subjects:
            subject_list = subjects.split(",")
            if not all(isinstance(s, str) and s.strip() != '' for s in subject_list):
                return jsonify({"error": "Invalid subject input. Please provide valid subject names."}), 400

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

        # Initialize the filter conditions list
        filters = []

        # Add subject filtering if requested
        if subjects:
            subject_list = subjects.split(",")  # Split subjects into a list
            filters.append(f"subjects.subject_name IN ({', '.join(['%s'] * len(subject_list))})")
            params.extend(subject_list)

        # Add color filtering if requested
        if colors:
            color_list = colors.split(",")  # Split colors into a list
            filters.append(f"colors.color_name IN ({', '.join(['%s'] * len(color_list))})")
            params.extend(color_list)

        # Add month filtering if requested
        if month:
            filters.append("MONTH(episodes.date) = %s")
            params.append(month)

        # Apply filter_type: 'any' or 'all'
        if filter_type == 'any':
            # If 'any', use OR for filters
            if filters:
                query += " WHERE " + " OR ".join(filters)
        else:
            # Default to 'all', using AND for filters
            if filters:
                query += " WHERE " + " AND ".join(filters)

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

    except Error as err:
        # Catch any database errors
        return jsonify({"error": f"Database error: {str(err)}"}), 500
    except Exception as e:
        # Catch any other errors
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
    finally:
        # Ensure cursor and connection are closed properly
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
