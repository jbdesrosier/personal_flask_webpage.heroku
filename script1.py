from flask import Flask, render_template, send_from_directory, url_for
#, resized_img_src
import os
#import flask_resize

app=Flask(__name__)

#app.config['RESIZE_URL'] = 'jbdesrosier.info/'
#app.config['RESIZE_ROOT'] = 'C:/Users/jbdes/Desktop/Flask/personal_site/'

#resize = flask_resize.Resize(app)

#app.secret_key='giraffe'
#images=Images(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contactInfo")
def contactInfo():
    return render_template("contactInfo.html")

@app.route("/CV")
def CV():
    return render_template("cv.html")
#    workingdir = os.path.abspath(os.getcwd())
#    filepath = workingdir + '/static/cv/'
#    return send_from_directory(filepath, "NBIF_Justin.pdf")

@app.route("/writing1")
def writing1():
    return render_template("writing1.html")

@app.route("/writing2")
def writing2():
    return render_template("writing2.html")

@app.route("/writing3")
def writing3():
    return render_template("writing3.html")

@app.route("/writing4")
def writing4():
    return render_template("writing4.html")

@app.route("/writing5")
def writing5():
    return render_template("writing5.html")

@app.route("/writing6")
def writing6():
    return render_template("writing6.html")

@app.route("/writing7")
def writing7():
    return render_template("writing7.html")

@app.route("/writing8")
def writing8():
    return render_template("writing8.html")

if __name__=="__main__":
    app.run(debug=True)
