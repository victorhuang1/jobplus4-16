#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, current_app, redirect, url_for, flash
from jobplus.forms import UserEditProfileForm

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/<int:user_id>')
def user_detail(user_id):
    return render_template('user/detail.html')


@user.route('/user/edit', methods=['GET', 'POST'])
def edit_user():
    form = UserEditProfileForm()
    return render_template('user/edit.html',form=form)


@user.route('/<int:user_id>/delivery')
def user_delivery(user_id):
    return render_template('user/delivery.html')
