from flask import Flask, request, render_template, redirect
import cgi      

app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route ('/') 
def index():
    return render_template('index.html')


def blank(x):
    if x:
        return True
    else:
        return False


def username_check(x):
    if len(x) < 3 or len(x) > 20:
        return False
    else:
        return True


def password_check(x):
    if len(x) < 3 or len(x) > 20:
        return False
    else:
        return True

def verify_password_check(x):
    return

def email_optional_check1(x):
    if x.count ('@') >= 1:
        return True
    else:
        return False

def email_optional_check2(x):
    if x.count ('.') >= 1:
        return True
    else:
        return False

@app.route ('/user-signup', methods=['POST'])
def user_signup_correct():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email_optional = request.form['email_optional']



    username_err = ""
    password_err = ""
    verify_password_err = ""
    email_optional_err = ""

    
    username_error = "username needs to be at least 3 characters and up to 20 characters"
    password_error = "password needs to be at least 3 characters and up to 20 characters"
    verify_password_error = "passwords need to match"
    email_optional_error = "email needs to have an @ symbol, contain no spaces, and a dot"
    
    #username errors
    
    if not blank(username):
        username_err = username_error
        username = ""

    else:
        if  not username_check(username):
            username_err = username_error
            username = ""
        
   
    #password errors
   
    if not password_check(password):
        password_err = password_error
        password = ""

   
    
    else:
        if not verify_password_check(password):
            password_err = password_error
            password = ""


    #email errors

    if not email_optional_check1(email_optional):
        email_optional_err = email_optional_error
        email = ""

    
    else:
        if email_optional_check2(email_optional):
            email_optional_err = email_optional_error
            email_optional = ""

    
    if not username_err and not password_err and not email_optional_err:
        username = username
        return redirect('index.html' username=username)
        

    else:
        return render_template ('index.html', username_error=username_error, username=username, password_error=password_error, )

    app.run()


