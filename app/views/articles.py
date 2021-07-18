from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_session, models

bp = Blueprint('articles', __name__, url_prefix='/articles')

@bp.route('/')
def index():
    s = get_session()
    a = s.query(models.Article).order_by(models.Article.date)[:10]
    return render_template('articles/index.html', articles=a)
