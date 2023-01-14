from Lock import open
from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route()

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
        open()
    else:
        status = 'Maglock is deactivated'
    return render_template('control.html', action=action, status=status)

if __name__ == '__main__':
    app.run()   
