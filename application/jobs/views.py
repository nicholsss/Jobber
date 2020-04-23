from application import app,db,login_manager,login_required
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.jobs.models import Job
from application.jobs.forms import JobForm
from application.auth.models import User
from application.questions.models import Question
from application.questions.forms import questionForm

@app.route("/jobs", methods=["GET"])
def jobs_index():

    if current_user.is_authenticated:
       return render_template("jobs/list.html", jobs = Job.interested_jobs(current_user.id))
   
    else:
        
            return render_template("jobs/list.html", jobs = Job.query.all())
        #try:
         #    return render_template("jobs/list.html", jobs = Job.interested_jobs(current_user.id))
        #except :
         
         #     return render_template("jobs/list.html", jobs = Job.query.all())
    
   

@app.route("/jobs/new/")
@login_required
def jobs_form():
    return render_template("jobs/new.html", form = JobForm())

@app.route("/jobs/edit/<job_id>/")
@login_required
def jobs_edit_form(job_id):
    return render_template("jobs/edit.html",job_id=job_id, form = JobForm())

@app.route("/jobs/view/<job_id>/")
def jobs_show(job_id):
    return render_template("jobs/job.html", form = questionForm(), job = Job.query.get(job_id), user= User.query.get(Job.query.get(job_id).account_id))

@app.route("/jobs/question/<job_id>/", methods =['POST'])
@login_required
def jobs_question(job_id):

    form = questionForm(request.form)

    r = Question(current_user.id, job_id, form.name.data)

    db.session().add(r)
    db.session().commit()
    return redirect(url_for("jobs_show",job_id=job_id))

@app.route("/jobs/<job_id>/", methods=['POST'])
@login_required
def jobs_edit(job_id):
    j = Job.query.get(job_id)

    if j.account_id != current_user.id:
   
        return login_manager.unauthorized()
    form = JobForm(request.form)
   
    if not form.validate():
         
         return render_template("jobs/edit.html", job_id=job_id, form = form)

    j.name = form.name.data
    j.salary = form.salary.data
    j.description = form.description.data
    
    db.session().commit()
    return redirect(url_for("jobs_index"))



@app.route("/jobs/active/<job_id>/", methods=["POST"])
@login_required
def jobs_set_active(job_id):
#Tästä tulee kiinnostunut, ja jokaisella käyttäjällä on on kiinostunt projektiin.
    

    j = Job.query.get(job_id)
    bol = False
    print("JOBIID", job_id)
    
    for x in current_user.interested:
        if x.id == j.id:
            bol = True
            print("KAVIKO", job_id)
    
    
    if(bol == False):
        j.intrest_user.append(current_user)
         #j.r.append(current_user)
    else:
        
        j.intrest_user.remove(current_user)
    db.session().commit()

  
    return redirect(url_for("jobs_index"))

@app.route("/jobs/delete/<job_id>/", methods=["POST"])
@login_required
def jobs_delete(job_id):
    j = Job.query.get(job_id)
    if j.account_id != current_user.id:
       #Tätä pitää vielä muokata, sillä ohjaa väärään paikkaan.
        return login_manager.unauthorized()
    
    Question.query.filter_by(job_id = job_id).delete()

    db.session().delete(j)
 
    db.session().commit()

    return redirect(url_for("jobs_index"))




@app.route("/jobs/", methods=["POST"])
@login_required
def jobs_create():
    form = JobForm(request.form)
    if not form.validate():
         
         return render_template("jobs/new.html", form = form)
    #j = Job(request.form.get("name"), request.form.get("salary"), current_user.id)
    j = Job(form.name.data, form.salary.data, form.description.data, current_user.id)

    db.session().add(j)

    #db.session().add(s)
    db.session().commit()

    

    return redirect(url_for("jobs_index"))

    