from . import auth
from flask import render_template
from .forms import LoginForm
@auth.route('/login',methods=['get','post'])
def login():
    form =LoginForm()
    return render_template('auth/login.html',form=form)