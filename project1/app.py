https://github.com/kevster555999/Project#!/user/bin/python

from flask import *

app=Flask(__name__)
app.secret_key= "myProjOfAwesomeNess"




#if __name__ = "__main__":

#-------
#OLD CODE BELOW

print "Hello World"


from flask import Flask
from flask import render_template
from flask import request
from flask import url_for, redirect, flash,session
from flask import *
import util
app = Flask(__name__)
app.secret_key = 'SWAGOVERFLOW'

questions=[]
rate=[]

File =  open("questions.txt")
for i in File.readlines():
    i=i.strip()
    #print i
    questions.append(i)
#print questions

@app.route("/")
def start():
    return redirect(url_for('login'))

@app.route("/login/",methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template("login.html")
    else:
        studentEmail=request.form['studentEmail']
        studentID=request.form['studentID']
        if(util.loginAuth(str(studentEmail),studentID)):
            session['user'] = request.form['studentEmail']#.encode('ascii','replace')
           # print session['user'] #debug
            return redirect(url_for('home'))
        else:
            return redirect(url_for('error'))

@app.route("/logout/",methods=['GET','POST'])
def logoff():
    session.pop('user',None)
    return redirect(url_for('login'))
    

@app.route("/home/",methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template("home.html")
    else:
        option=request.form['option']
        #if option == 'Rate':
         #   return redirect(url_for('Rate'))
        #if option == 'Your Ratings':
         #   return redirect(url_for('Your_Ratings'))
        if option == 'Logout':
            session.pop('user',None)
            return redirect(url_for('login'))
        pass

@app.route("/rate/",methods=['GET','POST'])
def Rate(yourGroup=None,questions=questions):
    if request.method=='GET':
        if 'user' in session:
            try:
                email = str(session['user'])
                yourGroup = util.getGroup(email)
                print yourGroup #debug
                return render_template('rate.html',groupmembers=yourGroup,questions=questions)
            except:
                return render_template('rate.html',groupmembers=["default@github.com"],questions=questions)
        else:
            return redirect(url_for("login"))
    else:
        submit = request.form['submit']
 #       option = request.form['option']
#        if submit == 'submit':
        for i in util.getGroup(str(session['user'])):
            for j in range(11):
                k=str(j)
                r = request.form[str(i+','+k)]
                rate.append(r)
                print r
            util.giveRating(session['user'],i,rate)
            rate = []
#        radio = request.form['radio']
#        for i in range (len(questions)):
#            print radio[i]
#            r = radio[i]
        #    rate = rate + r
        return redirect(url_for('home'))
#        if option == 'Back':
#            return render_template("home.html")
        #if option == 'Logout':
            #session.pop('user',None)
            #return redirect(url_for('login'))


@app.route("/yourRatings/",methods=['GET','POST'])
def yourRatings():
    if request.method=='GET':
        try:
            email = str(session['user'])
            #print email
            ratings = util.getAllRatings(email)
            #print ratings
            return render_template('yourRatings.html',ratings=ratings,questions=questions)
        except:
            try:
                return render_template('yourRatings.html')
            except:
                return redirect(url_for("login"))
        
    else:
        option=request.form['option']
        if option=='Back':
            return redirect(url_for('home'))
        pass

@app.route("/pastRatings/",methods=['GET','POST'])
def pastRatings():
    rated = None
    if request.method=='GET':
        if 'user' in session:
            try:
                email = str(session['user'])
                rated = util.ratingsGiven(email) #causes a key error when given a string in ascii
            except:
                pass
        return render_template('pastRatings.html',ratings=rated)
    else:
       option = request.form['option']
       if option == 'Back':
            return redirect(url_for('home'))
       pass

@app.route("/error/",methods=['GET','POST'])
def error(name=None,last=None):
    return render_template('error.html')

if __name__=="__main__":
    app.debug=True
    app.run(port=5005)
