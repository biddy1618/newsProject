from flask import (
    Blueprint, current_app,render_template, request
)

from sqlalchemy.sql.expression import func

import re
from sklearn.metrics.pairwise import linear_kernel

from app.db import get_session, models



bp = Blueprint('articles', __name__, url_prefix='/articles')

@bp.route('/', methods = ('GET', 'POST'))
def main():
    if request.method == 'POST':
        query = request.form['query']
        calendar = request.form['calendar']
        res = _get_top_n(query)
        ids, ranks = tuple(zip(*res))
        ids = [int(i) for i in ids]
        ranks = [float(i) for i in ranks]
        
        s = get_session()
        a = [(s.query(models.Article).get(id), ranks[i]) for i, id in enumerate(ids)]


        return render_template('articles/main.html', articles=a)

    s = get_session()
    a = s.query(models.Article).order_by(func.random())[:10]
    a = [(i, None) for i in a]
    return render_template('articles/main.html', articles=a)

def _preprocess(query):
    query = query.lower()
    query = re.sub('[\W_\d]+', ' ', query)
    query = current_app._mystem.lemmatize(query)
    query = ''.join(query)
    return query

def _get_top_n(query, n=10):
    q_transformed = _preprocess(query)
    q_transformed_body = current_app.tfidf_search['tfidf_body'].transform([q_transformed])
    q_transformed_title = current_app.tfidf_search['tfidf_title'].transform([q_transformed])

    dist_body = linear_kernel(q_transformed_body, current_app.tfidf_search['tfidf_body_matrix']).flatten()
    dist_title = linear_kernel(q_transformed_title, current_app.tfidf_search['tfidf_title_matrix']).flatten()

    b_weight = 0.3
    t_weight = 1 - b_weight

    dist_weighted = b_weight * dist_body + t_weight * dist_title
    top_n = dist_weighted.argsort()[-n:][::-1]
    return list(zip(current_app.tfidf_search['tfidf_index'][top_n], dist_weighted[top_n]))