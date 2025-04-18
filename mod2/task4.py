# app.py
from flask import Flask
from datetime import datetime

app = Flask(__name__)

weekdays = ['понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья']

@app.route('/hello-world/<name>')
def hello(name):
    weekday = weekdays[datetime.today().weekday()]
    return f'Привет, {name}. Хорошей {weekday}!'

if __name__ == '__main__':
    app.run(debug=True)
