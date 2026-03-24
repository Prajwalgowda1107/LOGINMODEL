from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

def get_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="project_db",
        cursorclass=pymysql.cursors.DictCursor
    )

# 🔐 LOGIN ROUTE
@app.route("/", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )
        user = cursor.fetchone()

        cursor.close()
        db.close()

        if user:
            # ✅ REDIRECT TO DASHBOARD
            return redirect(url_for('dashboard', user=username))
        else:
            message = "Invalid username or password ❌"

    return render_template("login.html", message=message)


# 🚀 DASHBOARD ROUTE
@app.route("/dashboard")
def dashboard():
    user = request.args.get('user')  # get username from URL
    return render_template("dashboard.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)