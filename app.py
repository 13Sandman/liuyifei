from flask import Flask,render_template

app = Flask(__name__)


@app.route('/liuyifei')
def he():  # put application's code here
    return render_template('portfolio-item.html')

@app.route('/liu')
def ll():  # put application's code here
    return render_template('post.html')

@app.route('/contact')
def lo_w():  # put application's code here
    return render_template('contact.html')

@app.route('/thankyou')
def world():  # put application's code here
    return render_template('thankyou.html')

@app.route('/fei')
def rld():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()