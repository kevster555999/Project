#!/user/bin/python

from flask import *

app=Flask(__name__)
app.secret_key= "myProjOfAwesomeNess"
#logged_in=False

@app.route("/")
def redirectHome():
    return redirect(url_for("home"))

@app.route("/home",methods=["GET","POST"])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        button = request.form["login"]
        if button == "login":
            Username = request.form["Username"]
            Password = request.form["Password"]
            if Username == "Kevin" and Password == "Huang":
                return redirect(url_for('success'))
            return redirect(url_for('failed'))

@app.route("/failed", methods=["GET","POST"])
def failed():
    if request.method == 'GET':
        return render_template("failed.html")
    if request.method == 'POST':
        button = request.form["back"]
        if button == "back":
            return redirect(url_for("home"))

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True,port = 9000)
