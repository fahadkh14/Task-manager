from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
import time

app = Flask(__name__)
CORS(app)

DB_HOST = os.getenv("DB_HOST", "mysql")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_NAME = os.getenv("DB_NAME", "taskdb")
DB_USER = os.getenv("DB_USER", "taskuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "taskpassword")


def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


# Wait for MySQL
for i in range(20):
    try:
        conn = get_connection()
        conn.close()
        print("Connected to MySQL")
        break
    except Exception:
        print("Waiting for MySQL...")
        time.sleep(3)


@app.route("/")
def home():
    return jsonify({
        "message": "Task Manager API Running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


@app.route("/tasks", methods=["GET"])
def get_tasks():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT id,title FROM tasks ORDER BY id DESC"
    )

    tasks = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():

    data = request.get_json()

    title = data.get("title")

    if not title:
        return jsonify({
            "error": "Title is required"
        }), 400

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks(title) VALUES(%s)",
        (title,)
    )

    conn.commit()

    task_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return jsonify({
        "id": task_id,
        "title": title
    }), 201


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "message": "Task deleted"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
