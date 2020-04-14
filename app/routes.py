# -*- coding: utf-8 -*-
from flask import render_template
from flask import request
from flask import redirect
from app import app
from app.coffee_house_db import Login

# from django-core import template  # всякие стандартные импорты
# register=template.Library()


@app.route('/')							# определяем основной путь
@app.route('/index')
def index():							# и соответствующий ему обработчик запросов
    return render_template('index.html')


@app.route('/wrong_add')
def wrong_add():
    return render_template('wrong_add.html')

@app.route('/add_new', methods=['GET', 'POST'])
# def add_new():
#     # form = DeadlineForm()
#     return render_template('add_form.html')

# @app.route('open_cashier_menu', methods=['POST'])
# def open_menu():
#     global

@app.route('/add_sale', methods=['POST'])
def add_sale():
    global _login, _password
    _login = request.form['login']
    _password = request.form['password']

    # check login and password
    if _login == 'cashier_1' and _password == '1234':
        print("logged as a cashier")
        current_user = Login(_login, _password, 1)
        return render_template('cashier_menu', cur_user=current_user)
    elif _login == 'administrator_1' and _password == '4321':
        print("logged as a cashier")
        current_user = Login(_login, _password, 0)
        return render_template('administrator_menu', cur_user=current_user)
    else:
        return redirect('wrong_add')
        # переход на страницу с оповещением о некорректности ввода


@app.route('/show_sales')
def show_new():
    list_of_sales = Sales.query.all()    # получаем лист наших дедлайнов (объектов типа Deadline)
    # list_of_titles = [str(list_of_deadlines.d_title)]
    # list_of_details = [str(list_of_deadlines.d_details)]
    return render_template('show_deadlines.html', cur_list=list_of_deadlines)