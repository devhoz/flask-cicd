from flask import Flask 

app = Flask (__name__)

@app.route ('/')

def hello():
    return '<h1> Hello, World!</h1>'

    app.debug=True 

@app.route ('/About/')

def about ():
    return' <h3> We at Devhoz technologies have around two years of IT experience</h3>'

@app.route ('/Contact/')

def contact ():
    return '<h4> To contact us, please sue the below form. Click on contact us </h4>'
