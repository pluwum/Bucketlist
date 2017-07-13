from flask import render_template, redirect, request, url_for
from app import app
from .bucketlist.bucket_list_app import BucketListApp
from .bucketlist.bucket_list import BucketList
from .bucketlist.bucket_list import Item

start_app = BucketListApp()



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
    if not start_app.current_user:
        return redirect(url_for('login'))
    elif len(start_app.current_user.bucket_lists) > 0:
        return render_template('home.html',
                               bucket_lists=start_app.current_user.bucket_lists)
    return render_template('home.html')


@app.route('/sign-out', methods=['GET'])
def sign_out():
    if start_app.current_user is not None:
        start_app.sign_out()
        return redirect(url_for('login'))
    return redirect(url_for('login'))


@app.route('/create_bucketlist', methods=['GET', 'POST'])
def create_bucketlist():
    if start_app.current_user is not None:
        if request.method == 'GET':
            return render_template('create-bucketlist.html')
        if request.method == 'POST':
            bucket_list_name = request.form['bucket_list_name']
            start_app.current_user.add_new_bucket_list(bucket_list_name)
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route('/viewbucketlist/<int:blist_id>', methods=['GET'])
def viewbucketlist(blist_id):
    start_app.current_bucketlist = blist_id
    if start_app.current_user is not None:
        if start_app.current_user.bucket_lists[blist_id].item_list:
            return render_template('bucketlist-item.html',
                                   users_buckets_items=start_app.current_user.bucket_lists[blist_id].item_list)
        return render_template('bucketlist-item.html',
                               users_buckets_items=start_app.current_user.bucket_lists[blist_id].item_list)
    else:
        return redirect(url_for('login'))


@app.route('/create_bucketlist_item', methods=['GET', 'POST'])
def create_bucketlist_item():
    if start_app.current_user is not None:
        if request.method == 'GET':
            return render_template('create-bucketlist-item.html')
        if request.method == 'POST':
            item_name = request.form['name']
            item_description = request.form['description']
            start_app.current_user.bucket_lists[start_app.current_bucketlist].add_bucket_list_item(item_name, item_description)
            return render_template('bucketlist-item.html',
                                   users_buckets_items=start_app.current_user.bucket_lists[start_app.current_bucketlist].item_list)
    return redirect(url_for('login'))