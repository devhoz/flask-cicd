
# Flask simple application
A simple application written in Flask using python.




Fork repository & copy the repository URL.

 Open your terminal & create a project dir
    
       mkdir project   
 Enter into your project dir & paste URL

       git clone https://github.com/devhoz/flask-cicd.git
 Make sure you have upgraded your pip3 latest version

       pip3 install --upgrade pip

 Now, create & activate your virtual environment 


       python3 -m venv venv  \\
       source venv/bin/activate
 After environment activated it should appear like below

       (venv) devhoz@debian$
 
 Now, Install the required dependencies into your virtual env

       (venv)$ pip install -r requirements.txt
    
 Finally, run the application

       (venv)$ flask run   
Now copy your localhost from below and paste it in your favourite browser 

  
       Serving Flask app 'app.py'
       Debug mode: off
       WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
       Running on http://127.0.0.1:5000


The application has the following endpoints:

       http://127.0.0.1:5000/       --displays index page
       http://127.0.0.1:5000/about  --displays app info






 

    




