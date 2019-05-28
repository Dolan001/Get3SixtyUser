"""
Handle all the authentication, session cookie process for user
"""
import hashlib

from flask import Blueprint, render_template, redirect, url_for, abort, request, session
from jinja2 import TemplateNotFound
import mysql.connector
from db_conn import *

authentication = Blueprint('auth', __name__)


@authentication.route('/error')
def error():
    try:
        return render_template('error.html')
    except TemplateNotFound:
        abort(404)


@authentication.route('/')
def index():
    if 'email' in session:
        try:
            return redirect(url_for('home.home'))
        except TemplateNotFound:
            abort(404)
    else:
        try:
            return render_template('index.html')
        except TemplateNotFound:
            abort(404)


@authentication.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.pop('email', None)
        email = request.form['email']
        pas = request.form['pass']
        print(email)
        # sha2 = hashlib.sha256(pas)
        # hex_dig = sha2.hexdigest().upper()
        if email == "" or pas == "":
            try:
                return redirect(url_for('auth.index'))
            except TemplateNotFound:
                abort(404)
        else:
            cursor.execute('select * from users where email="' + email + '" and password = "' + pas + '"')
            sql = cursor.fetchall()
            if len(sql) is 1:
                session['email'] = email
                print(session)
                try:
                    return redirect(url_for('home.home'))
                except TemplateNotFound:
                    abort(404)
            else:
                try:
                    return redirect(url_for('auth.error'))
                except TemplateNotFound:
                    abort(404)
    else:
        try:
            return redirect(url_for('home.home'))
        except TemplateNotFound:
            abort(404)


@authentication.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        pas = request.form['pass']
        conpas = request.form['conpass']
        phone = request.form['num']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        pcode = request.form['pcode']

        if fname == "" or lname == "" or email == "" or pas == "" or phone == "" or address == ""\
                or city == "" or state == "" or country == "" or pcode == "" or pas != conpas:
            try:
                return redirect(url_for('auth.index'))
            except TemplateNotFound:
                abort(404)
        else:
            sql = 'insert into users (firstname, lastname, email, password,phone_no,address,city, state, country,' \
                  'postal_code) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            val = (fname, lname, email, pas, phone, address, city, state, country, pcode)
            cursor.execute(sql, val)
            mydb.commit()
            try:
                return redirect(url_for('auth.index'))
            except TemplateNotFound:
                abort(404)
    else:
        try:
            return redirect(url_for('auth.index'))
        except TemplateNotFound:
            abort(404)


@authentication.route('/logout')
def logout():
    session.pop('email', None)
    try:
        return redirect(url_for('auth.index'))
    except TemplateNotFound:
        abort(404)


authentication.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
