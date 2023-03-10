from flask import Flask, render_template, request, redirect, url_for, make_response
from ArduinoCom import open_door, close_door



app = Flask(__name__, template_folder='html', static_folder='css')

@app.route('/')
def login():
    return render_template('main.html')


@app.route('/login-fourmz', methods=['POST'])
def loginpage():
    action = request.form['action']
    if action == 'Login': 
        return render_template ('login.html')


@app.route('/control', methods=['POST'])
def control():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'admin':
        return render_template('control.html')
    else:
        return render_template('login.html', message='Invalid credentials')

@app.route('/door', methods=['POST'])
def door():
    action = request.form['action']
    if action == 'Turn On':
        status = 'Maglock is activated'
        open_door()
    else:
        status = 'Maglock is deactivated'
        close_door()
    return render_template('control.html', action=action, status=status)

if __name__ == '__main__':
    app.run()   
