from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from app.db import get_session, models

bp = Blueprint('base', __name__)

@bp.route('/', methods=('GET', 'POST'))
def about():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        body = request.form['body']
        flash('Successfully submitted')
        flash(f'I will contact you, {name}, by the following e-mail: {email}.')
        
        return redirect(url_for('base.about', _anchor='contact'))
        
    return render_template('about.html')
