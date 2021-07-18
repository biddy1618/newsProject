from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_session, models

bp = Blueprint('index', __name__)

@bp.route('/')
def about():
    return render_template('about.html')
