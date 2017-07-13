"""Module containing routes for the bucket list app"""
from flask import render_template, redirect, request, url_for
from app import app
from .bucketlist.bucket_list_app import BucketListApp

BLISTAPP = BucketListApp()



@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    """function for user login"""
    if request.method == 'GET':
        return render_template('login.html', title='Sign In')
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        BLISTAPP.login_user(email, password)
        if BLISTAPP.current_user is not None:
            return redirect(url_for('home'))
        return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """function for user registration"""
    if request.method == 'GET':
        return render_template('register.html',
                               title='Register')
    if request.method == 'POST':
        user_fname = request.form['first_name']
        last_name = request.form['last_name']
        user_email = request.form['user_email']
        password = request.form['password']
        BLISTAPP.add_user(user_fname, last_name, user_email, password)
        return render_template('login.html',
                               title='Login')


@app.route('/home', methods=['GET'])
def home():
    """Function to render the home page"""
    if not BLISTAPP.current_user:
        return redirect(url_for('login'))
    elif BLISTAPP.current_user.bucket_lists:
        return render_template('home.html',
                               bucket_lists=BLISTAPP.current_user.bucket_lists)
    return render_template('home.html')


@app.route('/sign-out', methods=['GET'])
def sign_out():
    """User sign out function"""
    if BLISTAPP.current_user:
        BLISTAPP.sign_out()
        return redirect(url_for('login'))
    return redirect(url_for('login'))


@app.route('/create_bucketlist', methods=['GET', 'POST'])
def create_bucketlist():
    """function to create new a bucket list"""
    if BLISTAPP.current_user:
        if request.method == 'GET':
            return render_template('create-bucketlist.html')
        if request.method == 'POST':
            bucket_list_name = request.form['bucket_list_name']
            BLISTAPP.current_user.add_new_bucket_list(bucket_list_name)
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route('/viewbucketlist/<int:blist_id>', methods=['GET'])
def viewbucketlist(blist_id):
    """Function to view bucket list items of a particular bucket list"""
    BLISTAPP.current_bucketlist = blist_id
    if BLISTAPP.current_user:
        if BLISTAPP.current_user.bucket_lists[blist_id].item_list:
            return render_template('bucketlist-item.html',
                                   users_buckets_items=BLISTAPP.current_user.bucket_lists[blist_id].item_list)
        return render_template('bucketlist-item.html',
                               users_buckets_items=BLISTAPP.current_user.bucket_lists[blist_id].item_list)
    else:
        return redirect(url_for('login'))


@app.route('/create_bucketlist_item', methods=['GET', 'POST'])
def create_bucketlist_item():
    """function to create a bucket list item """
    if BLISTAPP.current_user:
        if request.method == 'GET':
            return render_template('create-bucketlist-item.html')
        if request.method == 'POST':
            item_name = request.form['name']
            item_description = request.form['description']
            BLISTAPP.current_user.bucket_lists[
                BLISTAPP.current_bucketlist].add_bucket_list_item(item_name, item_description)
            return render_template('bucketlist-item.html',
                                   users_buckets_items=BLISTAPP.current_user.bucket_lists[
                                       BLISTAPP.current_bucketlist].item_list)
    return redirect(url_for('login'))

@app.route('/delete_item/<int:item_id>', methods=['GET'])
def delete_bucketlist_item(item_id):
    """function to delete a bucket list item"""
    if BLISTAPP.current_user:
        item_name = BLISTAPP.current_user.bucket_lists[BLISTAPP.current_bucketlist].item_list[item_id].name
        BLISTAPP.current_user.bucket_lists[BLISTAPP.current_bucketlist].delete_bucket_list_item(item_name)
        return render_template('bucketlist-item.html',
                               users_buckets_items=BLISTAPP.current_user.bucket_lists[
                                   BLISTAPP.current_bucketlist].item_list)
    return redirect(url_for('login'))


@app.route('/edit_bucketlist_item/<int:item_id>', methods=['GET', 'POST'])
def edit_bucketlist_item(item_id):
    """function to edit a bucket list item"""
    if BLISTAPP.current_user:
        if request.method == 'POST':
            new_item_name = request.form['name']
            new_item_description = request.form['description']
            item_name = BLISTAPP.current_user.bucket_lists[BLISTAPP.current_bucketlist].item_list[item_id].name
            BLISTAPP.current_user.bucket_lists[
                BLISTAPP.current_bucketlist].edit_bucket_list_item(item_name, new_item_name, new_item_description)
            return render_template('bucketlist-item.html',
                                   users_buckets_items=BLISTAPP.current_user.bucket_lists[
                                       BLISTAPP.current_bucketlist].item_list,
                                   item_id=item_id)
        return render_template('bucketlist-item-edit.html',
                               item_details=BLISTAPP.current_user.bucket_lists[
                                   BLISTAPP.current_bucketlist].item_list[item_id],
                               item_id=item_id)
    return redirect(url_for('login'))


@app.route('/delete_bucketlist/<int:blist_id>', methods=['GET'])
def delete_bucketlist(blist_id):
    """function to delete a bucket list"""
    if BLISTAPP.current_user:
        bucket_list_name = BLISTAPP.current_user.bucket_lists[blist_id].name
        BLISTAPP.current_user.delete_bucket_list(bucket_list_name)
        return render_template('home.html',
                               bucket_lists=BLISTAPP.current_user.bucket_lists)
    return redirect(url_for('login'))


@app.route('/edit_bucketlist/<int:blist_id>', methods=['GET', 'POST'])
def edit_bucketlist(blist_id):
    """function to edit a bucket list"""
    if BLISTAPP.current_user:
        if request.method == 'POST':
            bucket_list_name = BLISTAPP.current_user.bucket_lists[blist_id].name
            new_bucketlist_name = request.form['bucket_list_name']
            BLISTAPP.current_user.edit_bucket_list(bucket_list_name, new_bucketlist_name)
            return redirect(url_for('home'))
        return render_template('bucketlist-edit.html',
                               bucket_list_details=BLISTAPP.current_user.bucket_lists[blist_id],
                               blist_id=blist_id)
