from flask import Flask, make_response

app = Flask(__name__)

'''
1. Для обработки ошибок я добавила декоратор errorhandler.
2. Для маршрута /reverse/ не добавила проверку, так как, если символов не будет, мы попадаем к errorhandler.
'''

@app.errorhandler(404)
def not_found(error):
    return make_response('Неправильные данные')

@app.route('/')
def hello():
    return "Это урок 2. Маршруты."

@app.route('/hello')
def greet():
    return  'Hello, world!'

@app.route('/info')
def information():
    return  'This is an informational page.'

@app.route('/calc/<int:num1>/<int:num2>')
def calculator_sum(num1, num2):
    return  f'The sum of {num1} and {num2} is {num1 + num2}.'

@app.route('/reverse/<text>')
def reverse_text(text):
    return text[::-1]

@app.route('/user/<name>/<int:age>')
def user_greet(name, age):
    if age <= 0:
        return 'Некорректный возраст'
    return f'Hello, {name}. You are {age} years old.'


if __name__ == "__main__":
    app.run(debug=True)