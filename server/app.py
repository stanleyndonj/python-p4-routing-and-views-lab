#!/usr/bin/env python3

from flask import Flask  # type: ignore

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<hello>")
def print_string(hello):
    print (hello)
    return hello

@app.route("/count/<parameter>")
def count(parameter):
    count = ""
    for i in range (10):
        count += f"{i}\n"
    return count

@app.route('/math/<int:num1>/<operator>/<int:num2>')
def perform_math(num1, operator, num2):
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    elif operator == '*':
        return str(num1 * num2)
    elif operator == 'div':
        return str(num1 / num2) if num2 != 0 else 'Error: Division by zero'
    elif operator == '%':
        return str(num1 % num2)
    else:
        return 'Error: Invalid operator'
    
    
