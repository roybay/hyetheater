from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.environ['MYSQL_HOSTNAME'],
            user=os.environ['MYSQL_USER'],
            passwd=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DATABASE']
        )
    except KeyError:
        print("one or more environment variables is/are not found")
    return connection


# Member API Route
@app.route("/members")
def members():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM members")
    member_emails = cursor.fetchall()
    cursor.close()
    conn.close()

    emails = [email[0] for email in member_emails]
    return jsonify(members=emails)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

