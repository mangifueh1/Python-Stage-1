import hashlib
from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from flask_login import current_user, login_user, login_required, logout_user

from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password Incorrect', category='success')
        else:
            flash('Email does not exist.', category='success')

    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['get', 'post'])
def sign_up():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        firstName = data.get('firstName')
        password1 = data.get('password1')
        password2 = data.get('password2')

        
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exist.', category='success')

        elif password1 == password2:
            new_user = User(email=email, first_name=firstName,
                            password=generate_password_hash(password1, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()

            login_user(user, remember=True)
            flash('Account created!', category='success')

            return redirect(url_for('views.home'))

        else:
            print('Error')

    return render_template('sign_up.html', user=current_user)
