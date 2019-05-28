"""
Handle all the requests and responses from and to home page
"""

from flask import Blueprint, render_template, abort, session, redirect, url_for, request, escape
from jinja2 import TemplateNotFound
from db_conn import cursor

homeReq = Blueprint('home', __name__)


@homeReq.route('/home', methods=['POST', 'GET'])
def home():
    if 'email' in session:
        cursor.execute('select * from products')
        product_list = cursor.fetchall()
        try:
            return render_template('home.html', product_list=product_list)
        except TemplateNotFound:
            abort(404)
    else:
        try:
            return redirect(url_for('auth.index'))
        except TemplateNotFound:
            abort(404)


@homeReq.route('/shop', methods=['POST', 'GET'])
def shop():
    if request.method == 'POST':
        search_product = request.form['search']
        if search_product == "":
            try:
                return redirect(url_for('home.home'))
            except TemplateNotFound:
                abort(404)
        else:
            cursor.execute('select * from products where product_name = "' + search_product +
                           '" or brand = "' + search_product + '" or category = "' + search_product +
                           '" order by product_name')
            search_res = cursor.fetchall()
            try:
                return render_template('shop.html', products=search_res)
            except TemplateNotFound:
                abort(404)
    else:
        if 'email' in session:
            email_session = session['email']
            cursor.execute('select * from products')
            product = cursor.fetchall()
            total = len(product)
            cursor.execute('select pr.*, ca.email from products pr, cart ca where'
                           ' pr.id = ca.product_id and ca.email = "' + email_session + '" and ca.sold = "0"')
            cart_item = cursor.fetchall()
            print(cart_item)
            try:
                return render_template('shop.html', products=product, total_product=total, cart_item=cart_item)
            except TemplateNotFound:
                abort(404)
        else:
            try:
                return redirect(url_for('auth.index'))
            except TemplateNotFound:
                abort(404)


@homeReq.route('/product/<product_id>/<product_name>', methods=['POST', 'GET'])
def product_details(product_id, product_name):
    if request.method == 'POST':
        return
    else:
        if 'email' in session:
            cursor.execute(
                'select * from products where id="' + product_id + '" and product_name = "' + product_name + '"')
            product = cursor.fetchone()
            try:
                return render_template('product-details.html', product=product)
            except TemplateNotFound:
                abort(404)
        else:
            try:
                return redirect(url_for('auth.index'))
            except TemplateNotFound:
                abort(404)


homeReq.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
