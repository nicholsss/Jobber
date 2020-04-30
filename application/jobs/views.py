from application import app, db, login_manager, login_required
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
        return render_template("jobs/list.html", user=current_user, jobs=Job.interested_jobs(current_user.id))

    else:

        return render_template("jobs/list.html", jobs=Job.query.all())

        
@app.route("/jobs/new/")
@login_required
def jobs_form():
    return render_template("jobs/new.html", form=JobForm())


@app.route("/jobs/myjobs")
@login_required
def my_jobs():
    return render_template("jobs/myjobs.html", user=current_user, jobs=Job.interested_jobs(current_user.id), job=current_user.jobs)


@app.route("/jobs/edit/<job_id>/")
@login_required
def jobs_edit_form(job_id):
    return render_template("jobs/edit.html", job_id=job_id, form=JobForm())


@app.route("/jobs/view/<job_id>/")
def jobs_show(job_id):
    if current_user.is_authenticated:
        return render_template("jobs/job.html", form=questionForm(), job=Job.query.get(job_id), users=current_user, user=User.query.get(Job.query.get(job_id).account_id))
    else:
        return render_template("jobs/job.html", form=questionForm(), job=Job.query.get(job_id),users=current_user, user=User.query.get(Job.query.get(job_id).account_id))


@app.route("/jobs/question/<job_id>/", methods=['POST'])
@login_required
def jobs_question(job_id):

    form = questionForm(request.form)

    r = Question(current_user.id, job_id, form.name.data)

    db.session().add(r)
    db.session().commit()
    return redirect(url_for("jobs_show", job_id=job_id))


@app.route("/jobs/<job_id>/", methods=['POST'])
@login_required
def jobs_edit(job_id):
    j = Job.query.get(job_id)

    if j.account_id != current_user.id and current_user.roles != 'ADMIN':

        return login_manager.unauthorized()
    form = JobForm(request.form)

    if not form.validate():

        return render_template("jobs/edit.html", job_id=job_id, form=form)

    j.name = form.name.data
    j.salary = form.salary.data
    j.description = form.description.data

    db.session().commit()
    return redirect(url_for("jobs_index"))


@app.route('/jobs/myjobs/<job_id>/', methods=["POST"])
@login_required
def job_set_done(job_id):
    j = Job.query.get(job_id)
    u = current_user
    bol = False

    u.earned = u.earned + j.salary

    for x in current_user.interested:
        if x.id == j.id:
            bol = True

    if(bol == False):
        j.intrest_user.append(current_user)

    else:

        j.intrest_user.remove(current_user)

    db.session().commit()

    return redirect(url_for("my_jobs"))


@app.route("/jobs/active/<job_id>/<k>/", methods=["POST"])
@login_required
def jobs_set_active(job_id, k):

    j = Job.query.get(job_id)
    bol = False
    for x in current_user.interested:
        if x.id == j.id:
            bol = True

    if(bol == False):
        j.intrest_user.append(current_user)

    else:

        j.intrest_user.remove(current_user)
    db.session().commit()

    if k == '1':
        return redirect(url_for("my_jobs"))

    else:

        return redirect(url_for("jobs_index"))

@app.route("/jobs/question/delete/<question_id>/", methods=["POST"])
@login_required
def question_delete(question_id):
    j = Question.query.get(question_id)
    if j.account_id != current_user.id and current_user.roles != 'ADMIN':

        return login_manager.unauthorized()

    db.session().delete(j)
    db.session().commit()

    return redirect(url_for("jobs_index"))

@app.route("/jobs/delete/<job_id>/", methods=["POST"])
@login_required
def jobs_delete(job_id):
    j = Job.query.get(job_id)
    if j.account_id != current_user.id and current_user.roles != 'ADMIN':

        return login_manager.unauthorized()

    Question.query.filter_by(job_id=job_id).delete()

    db.session().delete(j)
    db.session().commit()

    return redirect(url_for("jobs_index"))


@app.route("/jobs/", methods=["POST"])
@login_required
def jobs_create():
    form = JobForm(request.form)
    if not form.validate():

        return render_template("jobs/new.html", form=form)

    j = Job(form.name.data, form.salary.data,
            form.description.data, current_user.id)

    db.session().add(j)
    db.session().commit()

    return redirect(url_for("jobs_index"))
