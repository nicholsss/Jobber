from application import app,db
from flask import redirect, render_template, request, url_for
from application.jobs.models import Job

@app.route("/jobs", methods=["GET"])
def tasks_index():
    return render_template("jobs/list.html", jobs = Job.query.all())

@app.route("/jobs/new/")
def jobs_form():
    return render_template("jobs/new.html")

@app.route("/jobs/", methods=["POST"])
def jobs_create():
    j = Job(request.form.get("name"))
  
    db.session().add(j)
    db.session().commit()


    return redirect(url_for("jobs_index"))