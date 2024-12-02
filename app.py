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
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # Extract the 'month' query parameter
    month = request.args.get('month')  # E.g., "January"

    # SQL query to filter episodes by month
    if month:
        sql_query = """
        SELECT episode_id, episode, title, date
        FROM episodes
        WHERE MONTHNAME(date) = %s
        """
        cursor.execute(sql_query, (month,))
    else:
        sql_query = "SELECT episode_id, episode, title, date FROM episodes"
        cursor.execute(sql_query)

    # Fetch results and return as JSON
    episodes = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(episodes)

if __name__ == '__main__':
    app.run(debug=True)
