# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Time, Date

from app import db

# class Registration(db.Model):
#     __tablename__ = 'user'
#     user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
#     user_name = Column(String, unique=True)
# Это могло бы стать точкой расширения: e.g., добавление регистрации пользователей

# log_in table
class Login(db.Model):
    __tablename__ = 'log_in'
    login = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(30))
    occupation_id = db.Column(db.Integer)

    def __init__(self, login_, password_, occupation_id_):
        self.login = login_
        self.password = password_
        self.occupation_id = occupation_id_

# users_info table
class UsersInfo(db.Model):
    __tablename__ = 'users_info'
    login = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))

class Occupation(db.Model):
    __tablename__ = 'occupation'
    occupation_id = db.Column(db.Integer, primary_key=True)
    occupation = db.Column(db.String(30))

class Sales(db.Model):
    __tablename__ = 'sales'
    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)      # Primary key!
    sale_id = db.Column(db.Integer)                         # Unites a sale into one event
    cashier_login = db.Column(db.String(30))
    sale_date = db.Column(db.Date)
    d_time = db.Column(db.Time)
    product_id = db.Column(db.Integer)
    amount = db.Column(db.Integer)

    # def __init__(self, title, details, date, time):
    def __init__(self, sale_id_, cashier_login):
        self.sale_id = sale_id_.strip()
        self.cashier_login = cashier_login.strip()
        # self.d_date = date
        # self.d_time = time

    def save_sale(self):
        db.session.add(self)        # вызов add() добавляет объект
        db.session.commit()         # завершение транзакции


db.create_all()                     # создание бд по указанным параметрам
