"""Module containing routes for the bucket list app"""
from flask import render_template, redirect, request, url_for
from app import app
from .bucketlist.bucket_list_app import BucketListApp

blistapp = BucketListApp()



@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    """function for user login"""
    if request.method == 'GET':
        return render_template('login.html', title='Sign In')
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        blistapp.login_user(email, password)
        if blistapp.current_user is not None:
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
        blistapp.add_user(user_fname, last_name, user_email, password)
        return render_template('login.html',
                               title='Login')


@app.route('/home', methods=['GET'])
def home():
    """Function to render the home page"""
    if not blistapp.current_user:
        return redirect(url_for('login'))
    elif blistapp.current_user.bucket_lists:
        return render_template('home.html',
                               bucket_lists=blistapp.current_user.bucket_lists)
    return render_template('home.html')


@app.route('/sign-out', methods=['GET'])
def sign_out():
    """User sign out function"""
    if blistapp.current_user:
        blistapp.sign_out()
        return redirect(url_for('login'))
    return redirect(url_for('login'))


@app.route('/create_bucketlist', methods=['GET', 'POST'])
def create_bucketlist():
    """function to create new a bucket list"""
    if blistapp.current_user:
        if request.method == 'GET':
            return render_template('create-bucketlist.html')
        if request.method == 'POST':
            bucket_list_name = request.form['bucket_list_name']
            blistapp.current_user.add_new_bucket_list(bucket_list_name)
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route('/viewbucketlist/<int:blist_id>', methods=['GET'])
def viewbucketlist(blist_id):
    """Function to view bucket list items of a particular bucket list"""
    blistapp.current_bucketlist = blist_id
    if blistapp.current_user:
        if blistapp.current_user.bucket_lists[blist_id].item_list:
            return render_template('bucketlist-item.html',
                                   users_buckets_items=blistapp.current_user.bucket_lists[blist_id].item_list)
        return render_template('bucketlist-item.html',
                               users_buckets_items=blistapp.current_user.bucket_lists[blist_id].item_list)
    else:
        return redirect(url_for('login'))


@app.route('/create_bucketlist_item', methods=['GET', 'POST'])
def create_bucketlist_item():
    """function to create a bucket list item """
    if blistapp.current_user:
        if request.method == 'GET':
            return render_template('create-bucketlist-item.html')
        if request.method == 'POST':
            item_name = request.form['name']
            item_description = request.form['description']
            blistapp.current_user.bucket_lists[
                blistapp.current_bucketlist].add_bucket_list_item(item_name, item_description)
            return render_template('bucketlist-item.html',
                                   users_buckets_items=blistapp.current_user.bucket_lists[
                                       blistapp.current_bucketlist].item_list)
    return redirect(url_for('login'))

@app.route('/delete_item/<int:item_id>', methods=['GET'])
def delete_bucketlist_item(item_id):
    """function to delete a bucket list item"""
    if blistapp.current_user:
        item_name = blistapp.current_user.bucket_lists[blistapp.current_bucketlist].item_list[item_id].name
        blistapp.current_user.bucket_lists[blistapp.current_bucketlist].delete_bucket_list_item(item_name)
        return render_template('bucketlist-item.html',
                               users_buckets_items=blistapp.current_user.bucket_lists[
                                   blistapp.current_bucketlist].item_list)
    return redirect(url_for('login'))


@app.route('/edit_bucketlist_item/<int:item_id>', methods=['GET', 'POST'])
def edit_bucketlist_item(item_id):
    """function to edit a bucket list item"""
    if blistapp.current_user:
        if request.method == 'POST':
            new_item_name = request.form['name']
            new_item_description = request.form['description']
            item_name = blistapp.current_user.bucket_lists[blistapp.current_bucketlist].item_list[item_id].name
            blistapp.current_user.bucket_lists[
                blistapp.current_bucketlist].edit_bucket_list_item(item_name, new_item_name, new_item_description)
            return render_template('bucketlist-item.html',
                                   users_buckets_items=blistapp.current_user.bucket_lists[
                                       blistapp.current_bucketlist].item_list,
                                   item_id=item_id)
        return render_template('bucketlist-item-edit.html',
                               item_details=blistapp.current_user.bucket_lists[
                                   blistapp.current_bucketlist].item_list[item_id],
                               item_id=item_id)
    return redirect(url_for('login'))


@app.route('/delete_bucketlist/<int:blist_id>', methods=['GET'])
def delete_bucketlist(blist_id):
    """function to delete a bucket list"""
    if blistapp.current_user:
        bucket_list_name = blistapp.current_user.bucket_lists[blist_id].name
        blistapp.current_user.delete_bucket_list(bucket_list_name)
        return render_template('home.html',
                               bucket_lists=blistapp.current_user.bucket_lists)
    return redirect(url_for('login'))


@app.route('/edit_bucketlist/<int:blist_id>', methods=['GET', 'POST'])
def edit_bucketlist(blist_id):
    """function to edit a bucket list"""
    if blistapp.current_user:
        if request.method == 'POST':
            bucket_list_name = blistapp.current_user.bucket_lists[blist_id].name
            new_bucketlist_name = request.form['bucket_list_name']
            blistapp.current_user.edit_bucket_list(bucket_list_name, new_bucketlist_name)
            return redirect(url_for('home'))
        return render_template('bucketlist-edit.html',
                               bucket_list_details=blistapp.current_user.bucket_lists[blist_id],
                               blist_id=blist_id)
