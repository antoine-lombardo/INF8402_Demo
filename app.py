from flask import Flask, url_for, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ThisIsNotASecret:p"


USERS = [{
    'username': 'demo',
    'password': 'password'
}]


@app.route('/', methods=['GET'])
def index():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('index.html', message="Hello!")





@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form['username']
        p = request.form['password']
        found = False
        for user in USERS:
            if user['username'] == u:
                found = True
                pass
        if found:
            session['logged_in'] = True
            return redirect(url_for('index'))
        return render_template('index.html', message="Incorrect Details")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

if(__name__ == '__main__'):
    app.run()
