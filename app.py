from flask import Flask

app = Flask(__name__), render_template

@app.route('/'):
    return render_template('index.html')

@app.route('/register'):
    return render_template('register.html')

@app.route('/login'):
    return render_template('login.html')
