from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/calculate')
def calculator():
    num1=request.args.get('a', default=0, type=int)
    num2=request.args.get("b", default=0, type=int)
    operation=request.args.get("op")
    if operation == 'add':
        return str(num1 + num2)
    elif operation == 'sub':
        return str(num1 - num2)
    elif operation == 'mul':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    else:
        return "Invalid operation"
if __name__ == '__main__':
    app.run()