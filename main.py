from init import pam, basedat
from flask import render_template
#from flask_login import login_user, logout_user, UserMixin
from markupsafe import escape #render user input as text before processing | for all them sneaky users | but i don't neccessarily need it...
from flask import request as r
from function_house import take_user_data
from userbase import *

#why not just use sqlite3 isaac silas? why??

#i can't wait to try to hack myself!!!

#it's great to be able to implement previous knowledge as well ... o how i love creating scripts!

@pam.route("/")
def home_page():
    return render_template("pam_home.html")

@pam.route("/login")#sends a post request upon form submitting | "GET" requests are auto-accepted by flask servers then | the probability of any vunerability occuring depends on the platform used for implementing server
def login_page():
    return render_template("login.html")


@pam.route("/profile",methods=["POST"])#form valiadation occurs here | POST requests are accepted
def profile_page():
    if r.method == "POST":
        return "noneyet"
        
@pam.route("/make_account")
def signup_page():#create the database
                     #TODO: implement functionality for appending new users
    return render_template("pam_signup.html")  

@pam.route("/make_account/confirm",methods=["POST"])
def confirm_page():#lacking validation
    if r.method == "POST": 
        basedat.create_all()
        print('received data ',r.form)  #TODO: bypass this functionality 
        return render_template("confirm.html")

pam.run(host="127.0.0.10",port=8080,debug=True)

#to do - implement a mail server that will send requests, for example class-rep validations, to my email. I can then validate these requests and the system will handle all the rest
