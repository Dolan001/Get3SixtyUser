from flask import Blueprint, render_template, abort, session, redirect, url_for, request, escape
from jinja2 import TemplateNotFound
from db_conn import *

buy_pro = Blueprint('buy_product', __name__)


@buy_pro.route('/addCart/<product_id>/<product_name>')
def add_cart(product_id, product_name):
    email_session = escape(session['email']).capitalize()
    sql = 'insert into cart (email, product_id, product_name, sold) values(%s,%s,%s,%s)'
    val = (email_session, product_id, product_name, '0')
    cursor.execute(sql, val)
    mydb.commit()
    try:
        return redirect(url_for('home.shop'))
    except TemplateNotFound:
        abort(404)


buy_pro.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
