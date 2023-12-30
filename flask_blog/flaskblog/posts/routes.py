from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from .. import db # '..' means parent dir of the current dir
from ..modules.models import Post
from ..posts.forms import PostForm

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=['GET','POST'])
@login_required
def new_post():
    form=PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Aiit chief','success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
     # The query below works the same as normal 'query.get()' 
     # But in case what ever we parsed in doesn't work it returns a 404 error
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)  

@posts.route("/post/<int:post_id>/update", methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm() 

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data 
        db.session.commit()
        flash('Update sucessful','success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content

    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('main.home'))