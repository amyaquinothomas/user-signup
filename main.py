from flask import Flask, request, render_template, redirect
import cgi      

app = Flask(__name__)

app.config['DEBUG'] = True 
"""Need to do something with .format to get rid of the {0} that are on the signup page, 
   the app works I just ran it. But it will not show the errors just not sure where you need 
   to format it to get it to show errors. I just use flash now. Omar should know. 
"""

@app.route ("/") 
def index():
    return render_template('index.html')



@app.route ('/user_signup', methods=['POST'])
def user_signup():
    
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email_optional = request.form['email_optional']



    username_err = ""
    password_err = ""
    verify_password_err = ""
    email_optional_err = ""
    
    #username errors
    if len(username) < 3 or len(username) > 20 or " " in username:
        username_err = "username needs to be at least 3 characters and up to 20 characters"
        
    #password errors
   
    if len(password) < 3 or len(password) > 20 or " " in password:
        password_err = "password needs to be at least 3 characters and up to 20 characters"
        password = ''


    if verifypassword != password:
        verify_password_err = "passwords need to match"
        verifypassword = ''
   
    #email errors
    if email_optional != "":
        if email_optional.strip(' ') != email_optional:
            email_optional_err = 'Email cannot contain spaces. '
        elif '@' not in email_optional or '.' not in email_optional:
            email_optional_err = "email needs to have an @ symbol and a dot"
    #if email_optional != "" and email_optional != "@" in email_optional or email_optional != "." in email_optional:
        #email_optional_err = "email needs to have an @ symbol, contain no spaces, and a dot"

 
    if not email_optional_err and not password_err and not username_err and not verify_password_err:
        return render_template('welcome.html', username=username)
    
    else:
        return render_template('index.html', username_err=username_err, password_err=password_err, username=username, email_optional=email_optional, password=password, verify_password_err=verify_password_err, email_optional_err=email_optional_err, verifypassword=verifypassword)

app.run()


