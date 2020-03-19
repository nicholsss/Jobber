from application import app,db
from flask import redirect, render_template, request, url_for
from application.jobs.models import Job

@app.route("/jobs", methods=["GET"])
def jobs_index():
    return render_template("jobs/list.html", jobs = Job.query.all())

@app.route("/jobs/new/")
def jobs_form():
    return render_template("jobs/new.html")

@app.route("/jobs/<job_id>/", methods=["POST"])
def jobs_set_active(job_id):

    j = Job.query.get(job_id)
    j.active = True
   # if j == False:
      #  j.done = True
        
 #   elif j == True:
     #  j.done = False
    db.session().commit()
  
    return redirect(url_for("jobs_index"))

@app.route("/jobs/", methods=["POST"])
def jobs_create():

    j = Job(request.form.get("name"), request.form.get("salary"))
    #s = Job(request.form.get("salary"))

    db.session().add(j)

    #db.session().add(s)
    db.session().commit()

    return redirect(url_for("jobs_index"))