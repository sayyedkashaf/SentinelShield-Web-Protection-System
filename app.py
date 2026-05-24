import pandas as pd

from flask import Flask, request, render_template

from detector import detect_attack
from logger import log_event
from rate_limiter import is_rate_limited

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    user_input = request.form.get("input")

    ip = request.remote_addr

    # Rate Limiting Check
    if is_rate_limited(ip):

        log_event(
            ip,
            "Rate Limit Exceeded",
            "Blocked"
        )

        return "Blocked: Too Many Requests"

    # Attack Detection Check
    attack = detect_attack(user_input)

    if attack:

        log_event(
            ip,
            attack,
            "Blocked"
        )

        return f"Blocked: {attack} Detected"

    return "Request Allowed"

@app.route("/dashboard")
def dashboard():

    try:

        df = pd.read_csv(
            "logs/security_logs.csv"
        )

        total_events = len(df)

        table = df.to_html()

    except:

        total_events = 0

        table = "No Logs Available"

    return render_template(
        "dashboard.html",
        total_events=total_events,
        table=table
    )

if __name__ == "__main__":
    app.run(debug=True)