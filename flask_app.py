from flask import Flask
app = Flask(__name__)

@app.route('/first
def first():
    return render_template('first.html')
@app.route('/login
def login():
    return render_template('login.html')
