from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def success():
    account = request.args.get('account')
    return f"登录成功{account}"

app.run(debug=True)