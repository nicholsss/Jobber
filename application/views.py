from flask import render_template
from application import app
from application.auth.models import User
from application.jobs.models import Job

@app.route("/")
def index():
    return render_template("index.html", most_questions = User.most_questions_asked(), offers= Job.jobs_offers())