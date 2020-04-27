from application import app, db
from flask import redirect,render_template,request,url_for
from flask_login import login_required, current_user
from application.questions.models import Question
from application.questions.forms import questionForm

@app.route('reviews/new/')
@login_required
def reviews_form():
    return render_template("reviews/new.html", reviews = Review.query.all())

@app.route('/reviews/new/<job_id>/', methods=["POST"])
@login_required
