#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, current_app, redirect, url_for, flash
from jobplus.forms import LoginForm, RegisterForm

front = Blueprint('front', __name__)


@front.route('/')
def index():
    return render_template('index.html')


@front.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@front.route('/register')
def register():
    return render_template('register.html')
