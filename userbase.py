from init import pam, basedat
#log
from flask_login import UserMixin


class main_table(basedat.Model, UserMixin): #don't matter really
    
    matric = basedat.Column(basedat.String(10), primary_key = True) #integer cause of those zero values
    
    fname = basedat.Column(basedat.String(100), unique = False, nullable = False)

    oname = basedat.Column(basedat.String(100), unique = False, nullable = False)

    lname = basedat.Column(basedat.String(100), unique = False, nullable = False)

    basedatept = basedat.Column(basedat.String(100), unique = False, nullable = False)

    password = basedat.Column(basedat.String(100), unique = False, nullable = False)

    college = basedat.Column(basedat.String(10), unique = False, nullable = False)

    def __repr__(self): #customize printing out
        return f"User ( {self.matric},{self.fname},{self.oname},{self.lname},{self.dept},{self.password})"

    #basedat.create_all()#should be called within another action

class timetable(basedat.Model): #using the vars defined in userbase, and the config of e

    day = basedat.Column(basedat.String(10), primary_key = True)
    
    seven_to_nine = basedat.Column(basedat.String(10), nullable = False)


