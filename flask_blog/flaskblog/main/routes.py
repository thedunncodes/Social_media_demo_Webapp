from flask import render_template, Blueprint, request
from ..modules.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    post = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('index.html', Title='Home', posts=post)


@main.route("/about")
def about():
    post = Post.query.all()
    return render_template('about.html', Title='About', posts=post)