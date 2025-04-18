from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,world'

if __name__ == '__main__':
    app.run()
    

# when you think all control takes manually
# $env:FLASK_APP = "app_name.py"
# flask run
