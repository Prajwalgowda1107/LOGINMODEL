from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            return redirect(url_for('dashboard', user=username))
        else:
            message = "Invalid username or password ❌"

    return render_template("login.html", message=message)


@app.route("/dashboard")
def dashboard():
    user = request.args.get('user')
    return render_template("dashboard.html", user=user)


# ❌ REMOVE app.run() OR keep it safe:
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)