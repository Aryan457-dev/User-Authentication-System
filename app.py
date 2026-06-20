from flask import Flask, render_template, request, redirect, url_for, session
import random
from config import Config
from models import db, User

app = Flask(__name__)

app.config.from_object(Config)

app.secret_key = "supersecretkey"

db.init_app(app)


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(
            username=username,
            password=password
        ).first()

        if user:
            return redirect(url_for("dashboard"))

        return "<h3>Invalid Username or Password</h3>"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form["email"]

        user = User.query.filter_by(email=email).first()

        if user:

            otp = random.randint(100000, 999999)

            session["otp"] = str(otp)
            session["email"] = email

            print("Generated OTP:", otp)

            return redirect(url_for("verify_otp"))

        else:
            return "<h2>Email Not Found ❌</h2>"

    return render_template("forgot_password.html")

@app.route("/verify-otp", methods=["GET", "POST"])
def verify_otp():

    if request.method == "POST":

        entered_otp = request.form["otp"]

        if entered_otp == session["otp"]:
            return redirect(url_for("reset_password"))
        else:
            return "<h2>Invalid OTP ❌</h2>"

    return render_template("verify_otp.html")

@app.route("/reset-password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":

        new_password = request.form["new_password"]
        confirm_password = request.form["confirm_password"]

        if new_password != confirm_password:
            return "<h2> Password does not match </h2>"
        
        email = session.get("email")

        user = User.query.filter_by(email=email).first()

        if user:
            user.password = new_password 

            db.session.commit()

            session.pop("otp", None)
            session.pop("email", None)

            return redirect(url_for("login"))
        return "<h2>User not found </h2>"
    return render_template("reset_password.html")

if __name__ == "__main__":
    app.run(debug=True) 