from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(index.html)


@app.route('/signup_form')
def signup_form():
    return render_template(signup_form.html)


@app.route('/thankyou')
def thankyou():
    first = request.args.get('first')
    last = request.args.get('last')

    return render_template('ThankYou.html', first=first, last=last)

if __name__ == '__main__':
    app.run(debug=True)