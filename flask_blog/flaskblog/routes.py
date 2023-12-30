# NOTE: '.' in the importation code lines mean current directory.
#       therefore in our case 'flaskblog' since it's our package dir. 

# import os
# import secrets
# from flask import abort
# from PIL import Image # from Pillow package 
# from flask import render_template, url_for, flash, redirect, request
# from . import app, db, bcrypt, mail
# from .forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
# from .modules.models import User, Post
# from flask_login import login_user, current_user, logout_user, login_required
# from flask_mail import Message


# post = [
#     {
#         'Name': 'Gwensville Menk',
#         'DOB': 'August 25, 1996',
#         'Address': 'No.2 deanut street, yorsville, Nigeria.',
#         'possession': 'Honda Nsx Type R'
#     },
#     {
#         'Name': 'kunle Afuwape',
#         'DOB': 'September 26, 1998',
#         'Address': 'No.14, Arubiewe, near London street, Magodo Nigeria.',
#         'possession': 'Mazda RX7 and 2 story Duplex'
#     }
# ]

# with app.app_context():
#     db.create_all()

# @app.route("/")
# @app.route("/home")
# def home():
#     page = request.args.get('page', 1, type=int)
#     post = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
#     return render_template('index.html', Title='Home', posts=post)


# @app.route("/about")
# def about():
#     post = Post.query.all()
#     return render_template('about.html', Title='About', posts=post)

# @app.route("/register", methods=['GET','POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         user = User(username=form.username.data, email=form.email.data, password=hashed_password)
#         db.session.add(user)
#         db.session.commit()
#         flash(f'{form.username.data}, Your account has now been created! You can now proceed to log in.', 'success')
#         return redirect(url_for('login'))
#     return render_template('register.html', Title='Register',form=form)

# @app.route("/login", methods=['GET','POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             login_user(user, remember=form.remember.data)
#             next_page = request.args.get('next')
#             flash(f'{user.username}, welcome', 'success')
#             return redirect(next_page) if next_page else redirect(url_for('home'))
#         else:
#             flash(f'Login Unsucessful. Please check email and password', 'danger')
#     return render_template('login.html', Title='Login',form=form)

# @app.route("/logout")
# def logout():
#     logout_user()
#     return redirect(url_for('home'))

# def save_picture(form_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext, = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
#     # To automatically resize any image sent in to 125px

#     output_size = (125, 125)
#     i = Image.open(form_picture)
#     i.thumbnail(output_size)
#     i.save(picture_path)
    
#     # Since 'i' will be the new image we want we'll save that instead of 'form_picture'
#     # resizing pictures helps in reducing size there by loading website's faster
#     # Discarded: form_picture.save(picture_path)

#     return picture_fn 

# @app.route("/account", methods=['GET','POST'])
# @login_required
# def account():
#     form = UpdateAccountForm()
#     if form.validate_on_submit():
#         if form.picture.data:
#             picture_file = save_picture(form.picture.data)
#             current_user.image_file = picture_file
#         current_user.username = form.username.data
#         current_user.email = form.email.data
#         db.session.commit()
#         flash(f'Your account has been updated!', 'success')
#         return redirect(url_for('account'))
#     elif request.method == 'GET': 
#         form.username.data = current_user.username
#         form.email.data = current_user.email
#     image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
#     return render_template('account.html', Title='Account', image_file=image_file, form=form)


# @app.route("/post/new", methods=['GET','POST'])
# @login_required
# def new_post():
#     form=PostForm()
#     if form.validate_on_submit():
#         post = Post(title=form.title.data, content=form.content.data, author=current_user)
#         db.session.add(post)
#         db.session.commit()
#         flash('Aiit chief','success')
#         return redirect(url_for('home'))
#     return render_template('create_post.html', title='New Post', form=form, legend='New Post')


# @app.route("/post/<int:post_id>")
# def post(post_id):
#      # The query below works the same as normal 'query.get()' 
#      # But in case what ever we parsed in doesn't work it returns a 404 error
#     post = Post.query.get_or_404(post_id)
#     return render_template('post.html', title=post.title, post=post)  

# @app.route("/post/<int:post_id>/update", methods=['GET','POST'])
# @login_required
# def update_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     form = PostForm() 

#     if form.validate_on_submit():
#         post.title = form.title.data
#         post.content = form.content.data 
#         db.session.commit()
#         flash('Update sucessful','success')
#         return redirect(url_for('post', post_id=post.id))
#     elif request.method == 'GET':
#         form.title.data = post.title
#         form.content.data = post.content

#     return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

# @app.route("/post/<int:post_id>/delete", methods=['POST'])
# @login_required
# def delete_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     db.session.delete(post)
#     db.session.commit()
#     flash('Your post has been deleted', 'success')
#     return redirect(url_for('home'))

# @app.route("/user/<string:username>")
# def user_posts(username):
#     page = request.args.get('page', 1, type=int)
#     user = User.query.filter_by(username=username).first_or_404()
#     post = Post.query.filter_by(author=user)\
#         .order_by(Post.date_posted.desc())\
#             .paginate(page=page, per_page=2)
#     # the below is same as above, just showing how to properly split code lines
#     # post = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=1)
#     return render_template('user_posts.html', Title='Home', posts=post, user=user)

# def send_reset_email(user):
#     token = user.get_reset_token()
#     msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
#     msg.body = f'''To reset your password visit the following link:
# { url_for('reset_token', token=token, _external=True) }

# NOTE: This email is only valid for 5 minutes.
# if you did not make this request, simply ignore this email and no changes will be made.
# '''
#     mail.send(msg)
#     return "sent"

# @app.route("/reset_password", methods=['GET','POST'])
# def reset_request():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = RequestResetForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         send_reset_email(user)
#         flash('An email has been sent with instructions to reset your password.', 'info')
#         return redirect(url_for('login'))
#     return render_template('reset_request.html', Title='Reset Password', form=form)

# @app.route("/reset_password/<token>", methods=['GET','POST'])
# def reset_token(token):
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     user = User.verify_reset_token(token)
#     if user is None:
#         flash('That is an invalid or expired token', 'warning')
#         return redirect(url_for('reset_request'))
#     form = ResetPasswordForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         user.password = hashed_password
#         db.session.commit()
#         flash(f'{user.username}, Your password has been updated! You can now proceed to log in.', 'success')
#         return redirect(url_for('login'))
#     return render_template('reset_token.html', Title='Reset Password', form=form)