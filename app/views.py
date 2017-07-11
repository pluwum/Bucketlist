from flask import render_template, flash, redirect, request, abort
from app import app
import os



@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
        return render_template('login.html',
                           title='Sign In')



@app.route('/bucketlist')
def bucketlist():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('bucketlist.html',
                           title='Home',
                           user=user)