from flask import render_template, request

from config import app
from models.user import User


@app.route('/')
def login_template():
        return render_template('login.html')


@app.route('/register')
def register_template():
        return render_template('register.html')


@app.route('/login-validation', methods=['POST'])
def login_validation():
        uname = request.form.get('username')
        password = request.form.get('password')
        users = User.return_users()
        print(users)
        existing_user = User.get_user_by_uname(uname)

        if existing_user.password != password:
                return "<h1>Invalid Credentials</h1>"

        return "<h1>Welcome Back {}</h1>".format(uname)


@app.route('/register-validation', methods=['POST'])
def register_validations():
        try:
                username = request.form.get('username')
                password = request.form.get('password')
                User.create_user(username, password)
                return {
                        "status": "success",
                        "message": f"User created successfully {username}"
                }
        except Exception as e:
                return "There was an error creating the user: {}".format(e)


if __name__ == '__main__':
        app.run()
