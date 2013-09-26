#!/user/bin/python

from flask import *

app=Flask(__name__)
app.secret_key= "myProjOfAwesomeNess"
logged_in=False

@app.route("/HomePage",methods=["Get","Post"])
def run():
    if request.method == 'Get' :
        return render_template("home.html")
    else:
        


if __name__ == "__main__":
    app.run(debug=True,port = 9000)
