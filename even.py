from flask import Flask
app =Flask(__name__)
@app.route('/')
def evenprime(n):
    if n % 2 == 0 :
    
if __name__=='__main__':
    app.run()   