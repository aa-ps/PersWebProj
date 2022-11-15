from flask import Flask, render_template, request
from functions import readDetails

website = Flask(__name__)

myName = "Aaron Pulido Salinas"
myBio = readDetails("static/bio.txt")


@website.route("/")
def indexPage():
    return render_template("index.html", name=myName, aboutMe=myBio)


@website.route("/contact", methods=['GET', 'POST'])
def contactPage():
    name = None
    message = None
    if request.method == 'POST':
        name=request.form['name']
        message = request.form["message"]
    return render_template('contact.html', name=name, message=message)
