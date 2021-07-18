from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app.db import get_session, models

bp = Blueprint('base', __name__)

@bp.route('/')
def about():
    return render_template('about.html')
