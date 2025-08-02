from flask import Flask
app =Flask(__name__)


@app.route('/<name>')
def hello_name(name):
    msg= '<h1>hello %s</h1>' % name
    msg += '<p> welcome to flask</p>'
    msg += '<p> enjoy your stay</p>'
    msg +='<p>have a great day </p>'
    return msg

if __name__=='__main__':
    app.run()
