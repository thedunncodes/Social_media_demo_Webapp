import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from .. import app, mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext, = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    # To automatically resize any image sent in to 125px

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    # Since 'i' will be the new image we want we'll save that instead of 'form_picture'
    # resizing pictures helps in reducing size there by loading website's faster
    # Discarded: form_picture.save(picture_path)

    return picture_fn 

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password visit the following link:
{ url_for('users.reset_token', token=token, _external=True) }

NOTE: This email is only valid for 5 minutes.
if you did not make this request, simply ignore this email and no changes will be made.
'''
    mail.send(msg)
    return "sent"