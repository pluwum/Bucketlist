from flask import render_template, redirect, request, url_for, session
from app import app
from .bucketlist.bucket_list_app import BucketListApp

start_app = BucketListApp()
app.secret_key = 'F12Zr47j3yX R~X@H!jmM]Lwf/,?KT'

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', title='Sign In')
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        start_app.login_user(email, password)
        if start_app.current_user is not None:
            return redirect(url_for('home'))
        return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html',
                               title='Register')
    if request.method == 'POST':
        user_fname = request.form['first_name']
        last_name = request.form['last_name']
        user_email = request.form['user_email']
        password = request.form['password']
        start_app.add_user(user_fname, last_name, user_email, password)
        return render_template('login.html',
                               title='Login')


@app.route('/home', methods=['GET'])
def home():
    if start_app.current_user is None:
        return redirect(url_for('login'))
    return render_template('home.html')


@app.route('/sign-out', methods=['GET'])
def sign_out():
    if start_app.current_user is not None:
        start_app.sign_out()
        redirect(url_for('login'))
    redirect(url_for('login'))