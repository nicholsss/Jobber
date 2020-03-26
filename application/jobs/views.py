from application import app,db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.jobs.models import Job
from application.jobs.forms import JobForm

@app.route("/jobs", methods=["GET"])
def jobs_index():
    return render_template("jobs/list.html", jobs = Job.query.all())

@app.route("/jobs/new/")
@login_required
def jobs_form():
    return render_template("jobs/new.html", form = JobForm())

@app.route("/jobs/<job_id>/", methods=["POST"])
@login_required
def jobs_set_active(job_id):

    j = Job.query.get(job_id)
    #j.active = True

    if(j.active == False):
        j.active=True
    else:
        j.active=False
    db.session().commit()

  
    return redirect(url_for("jobs_index"))

@app.route("/jobs/", methods=["POST"])
@login_required
def jobs_create():

    form = JobForm(request.form)

    if not form.validate():
         
         return render_template("jobs/new.html", form = form)
    j = Job(request.form.get("name"), request.form.get("salary"), current_user.id)
    #j = Job(form.name.data, form.salary.data)
    #j.salary = form.salary.data
    #s = Job(request.form.get("salary"))
    #j.account_id = current_user.id

   

    db.session().add(j)

    #db.session().add(s)
    db.session().commit()

    

    return redirect(url_for("jobs_index"))