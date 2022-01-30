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

if __name__=="__main__":
    app.run(debug=True)
