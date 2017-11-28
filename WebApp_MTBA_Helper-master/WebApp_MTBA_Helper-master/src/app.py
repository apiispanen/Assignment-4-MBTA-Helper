from flask import Flask, render_template, request

from mbta_helper import find_stop_near

app = Flask(__name__)

app.config['DEBUG'] = True

app.secret_key = "Some secret string here"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        intad = request.form['location']
        result = find_stop_near(intad)

        if result:
            return render_template('results.html',intad=intad, result=result)
        else:
            return render_template('index.html', error=True)
    return render_template('index.html', error=None)



@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        name = name.upper()
    return render_template('hello.html', name=name)



if __name__ == '__main__':
    app.run()