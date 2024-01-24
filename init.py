    #instiantate my global variables
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

pam = Flask("pamela")#spawn a flask object
kasa = Flask("kasa")
anki = Flask("anki")

pam.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///2021.db'

basedat = SQLAlchemy(pam) #main database, rooting to main Flask object

timetable = SQLAlchemy() #id prefer not to have this functionality
#f = SQLAlchemy() #dont know what exactly i need u for tho


#log = LoginManager(pam)  #log manager, rooted to main database, which will be used for authenticating users1

#first attain the user's department
#determine the college
#obtain class data from table using time range and college
#i.e timetable.get(timerange = str(gettimerange(time.currenttime()), college = "COLENG")

#TODO: find means to express table header, and make sure functions are in O(1) as much as possible

