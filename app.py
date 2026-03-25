from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 🔐 LOGIN ROUTE
@app.route("/", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":   # ✅ THIS WAS MISSING
        username = request.form["username"]
        password = request.form["password"]

        # ✅ TEMP LOGIN (no database)
        if username == "admin" and password == "123":
            return redirect(url_for('dashboard', user=username))
        else:
            message = "Invalid username or password ❌"

    return render_template("login.html", message=message)


# 🚀 DASHBOARD ROUTE
@app.route("/dashboard")
def dashboard():
    user = request.args.get('user')
    return render_template("dashboard.html", user=user)


if __name__ == "__main__":
    app.run()