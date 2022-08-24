from flask import Flask 

app = Flask (__name__)

@app.route ('/')

def hello():
    return '<h1> Hello, World Testing!</h1>'

    app.debug=True 

@app.route ('/About/')

def about ():
    return' <h3> This is simple flask application made using python deployed on Elastic Bean Stalk (EBS).</h3>'


