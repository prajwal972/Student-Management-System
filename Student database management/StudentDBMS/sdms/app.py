from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "sdms_secret_key_2024"


DB_HOST     = "localhost"
DB_USER     = "root"
DB_PASSWORD = "Ssspk18@" 
DB_NAME     = "student_management"



def get_connection():
    """Open and return a MySQL connection. Returns None on failure."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except Error as e:
        print(f"[DB ERROR] {e}")
        return None

@app.route("/")
def index():
    conn = get_connection()
    students = []
    if conn:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM students ORDER BY id DESC")
        students = cur.fetchall()
        cur.close()
        conn.close()
    else:
        flash("Cannot connect to database. Check DB_PASSWORD in app.py", "error")
    return render_template("index.html", students=students)

@app.route("/search")
def search():
    q = request.args.get("q", "").strip()
    if not q:
        return redirect(url_for("index"))
    conn = get_connection()
    students = []
    if conn:
        cur = conn.cursor(dictionary=True)
        like = f"%{q}%"
        cur.execute(
            "SELECT * FROM students WHERE name LIKE %s OR roll_no LIKE %s ORDER BY id DESC",
            (like, like)
        )
        students = cur.fetchall()
        cur.close()
        conn.close()
    return render_template("index.html", students=students, query=q)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name    = request.form["name"].strip()
        roll_no = request.form["roll_no"].strip()
        course  = request.form["course"].strip()
        email   = request.form["email"].strip()
        phone   = request.form["phone"].strip()

        if not all([name, roll_no, course, email, phone]):
            flash("All fields are required!", "error")
            return render_template("add.html")

        conn = get_connection()
        if not conn:
            flash("Database connection failed.", "error")
            return render_template("add.html")

        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO students (name, roll_no, course, email, phone) VALUES (%s,%s,%s,%s,%s)",
                (name, roll_no, course, email, phone)
            )
            conn.commit()
            flash(f"Student '{name}' added successfully!", "success")
            return redirect(url_for("index"))
        except Error as e:
            conn.rollback()
            if e.errno == 1062:
                flash(f"Roll No '{roll_no}' already exists!", "error")
            else:
                flash(f"Error: {e}", "error")
            return render_template("add.html")
        finally:
            cur.close()
            conn.close()

    return render_template("add.html")


@app.route("/update/<int:sid>", methods=["GET", "POST"])
def update(sid):
    conn = get_connection()
    if not conn:
        flash("Database connection failed.", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        name    = request.form["name"].strip()
        roll_no = request.form["roll_no"].strip()
        course  = request.form["course"].strip()
        email   = request.form["email"].strip()
        phone   = request.form["phone"].strip()
        try:
            cur = conn.cursor()
            cur.execute(
                "UPDATE students SET name=%s, roll_no=%s, course=%s, email=%s, phone=%s WHERE id=%s",
                (name, roll_no, course, email, phone, sid)
            )
            conn.commit()
            flash(f"Student '{name}' updated successfully!", "success")
            return redirect(url_for("index"))
        except Error as e:
            conn.rollback()
            flash(f"Error: {e}", "error")
            return redirect(url_for("index"))
        finally:
            cur.close()
            conn.close()
    else:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM students WHERE id=%s", (sid,))
        student = cur.fetchone()
        cur.close()
        conn.close()
        if not student:
            flash("Student not found.", "error")
            return redirect(url_for("index"))
        return render_template("update.html", student=student)


@app.route("/delete/<int:sid>", methods=["POST"])
def delete(sid):
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT name FROM students WHERE id=%s", (sid,))
            row = cur.fetchone()
            cur.execute("DELETE FROM students WHERE id=%s", (sid,))
            conn.commit()
            name = row[0] if row else "Student"
            flash(f"'{name}' deleted successfully.", "success")
        except Error as e:
            conn.rollback()
            flash(f"Error: {e}", "error")
        finally:
            cur.close()
            conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    print("\n✅ Server starting at: http://127.0.0.1:5001\n")
    app.run(debug=True, port=5001)
