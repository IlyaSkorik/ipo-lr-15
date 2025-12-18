from flask import request, jsonify
from app import app


@app.route('/')
def index():
    return "Добро пожаловать в сервис!"

@app.route('/hello/<name>')
def hello(name):
    return f"Привет, {name}!"

@app.route('/square/<int:number>')
def square(number):
    result = number ** 2
    return f"Квадрат числа {number} равен {result}."

@app.route('/json', methods=['POST'])
def handle_json():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Ожидался JSON"}), 400
    name = data.get("name")
    age = data.get("age")
    if name is None or age is None:
        return jsonify({"error": "Требуются поля 'name' и 'age'"}), 400
    try:
        age = int(age)
    except (TypeError, ValueError):
        return jsonify({"error": "Поле 'age' должно быть числом"}), 400
    message = f"Привет, {name}! Тебе {age} лет."
    return jsonify({"message": message})

@app.route('/multiply/<a>/<b>')
def multiply(a, b):
    try:
        num_a = float(a)
        num_b = float(b)
        result = num_a * num_b
        return jsonify({"a": num_a, "b": num_b, "product": result})
    except ValueError:
        return jsonify({"error": "Оба параметра должны быть числами"}), 400