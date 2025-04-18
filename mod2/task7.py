# app.py
from flask import Flask, abort
from datetime import datetime
import os

app = Flask(__name__)

weekdays = ['понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья']

@app.route('/hello-world/<name>')
def hello(name):
    weekday = weekdays[datetime.now().weekday()]
    return f'Привет, {name}. Хорошей {weekday}!'

@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    try:
        nums = [int(n) for n in numbers.split('/') if n.isdigit()]
        if not nums:
            return 'Ошибка: числа не найдены'
        return f'Максимальное число: {max(nums)}'
    except ValueError:
        return 'Ошибка: переданы нечисловые значения'

@app.route('/preview/<int:size>/<path:relative_path>')
def preview(size, relative_path):
    abs_path = os.path.abspath(relative_path)

    # Security check:  Don't allow going outside the current directory.
    if not abs_path.startswith(os.getcwd()):
        abort(400, description="Invalid path:  Must be within the current directory.")

    try:
        with open(abs_path, 'r', encoding='utf-8') as f:
            result_text = f.read(size)
        return f"<b>{abs_path}</b> {len(result_text)}<br>{result_text}"
    except FileNotFoundError:
        abort(404, description=f"File not found: {abs_path}")
    except Exception as e:
        return f'Ошибка: {e}'

# Expenses tracking:
expenses = {}  # Initialize expenses dictionary at the module level

@app.route('/add/<date>/<int:number>')
def add(date, number):
    if len(date) != 6 or not date.isdigit():
        return "Ошибка: Неверный формат даты (YYYYMM)."

    try:
        year = int(date[:4])
        month = int(date[4:6])

        # Validate month (optional, but good practice)
        if not 1 <= month <= 12:
            return "Ошибка: Неверный месяц. Должен быть от 1 до 12."

        expenses.setdefault(year, {}).setdefault(month, 0)
        expenses[year][month] += number
        return f'Добавлено: {number} рублей за {year}-{month}'
    except ValueError:
        return "Ошибка: Невозможно преобразовать дату в число."

@app.route('/calculate/<int:year>')
@app.route('/calculate/<int:year>/<int:month>')
def calculate(year, month=None):
    if year not in expenses:
        return 'Нет данных'

    if month:
        if month not in expenses[year]:
            return "0" #Return 0 not an error if month doesn't exist
        return str(expenses[year][month])

    return str(sum(expenses[year].values()))

if __name__ == '__main__':
    app.run(debug=True)