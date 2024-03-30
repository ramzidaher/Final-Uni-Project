from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/explore')
def features():
    return render_template('explore.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
