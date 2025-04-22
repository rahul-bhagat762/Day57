from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>"+ function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>"+ function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>"+ function() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style ="text-align:center">Hello,world</h1>' \
    '<p>This is my paragraph.</p>' \
    '<img src = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjNpdnhocnBhd29kd2hsZHM1ZDM0YjZicWZiNXZnNzdicjh0dzZueiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriO0OEd9QIDdllqo/giphy.gif" width = 200px>'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

# @app.route("/username/<name>")
# def greet(name):
#     return f"Hello {name}"

@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"Hello {name}, you are {number} years old!" 

if __name__ == '__main__':
    app.run(debug=True)
