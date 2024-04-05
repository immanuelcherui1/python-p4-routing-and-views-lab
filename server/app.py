#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:display>')
def print_string(display):
    print (f"{display}")
    return display

@app.route('/count/<int:number>')
def count(number):
    output = ""
    for i in range(number):
        output += f"{i}\n"
    return output


@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return (num1 - num2)
    elif operation == "*":
        return (num1 * num2)
    elif operation == "div":
        if num2 != 0:
            return (num1 / num2)
        else:
            return "Error: Division by zero"
    elif operation == "%":
        return (num1 % num2)
    else:
        return ("use correct operation")
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
