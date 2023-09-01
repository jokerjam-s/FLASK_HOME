from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main.html')

    response = make_response(redirect('/hello/'))
    response.set_cookie('username', request.form.get('user_name'))
    response.set_cookie('usermail', request.form.get('user_mail'))

    return response


@app.route('/hello/')
def hello():
    content = {
        'user_name': request.cookies.get('username'),
        'user_mail': request.cookies.get('usermail')
    }
    return render_template('hello.html', **content)


@app.route('/logout/')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('username')
    response.delete_cookie('usermail')
    return response


if __name__ == '__main__':
    app.run(debug=True)