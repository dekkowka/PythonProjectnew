import random
from flask import Flask
from datetime import datetime, timedelta
import os
import re

app = Flask(__name__)

cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
visits = 0
time_format = '%d.%m.%Y %H:%M:%S'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
WORDS = []


def load_words():
    global WORDS
    try:
        with open(BOOK_FILE, 'r', encoding='utf-8') as book:
            text = book.read()
            WORDS = re.findall(r'\b\w+\b', text)
    except FileNotFoundError:
        print(f"Error: File not found at {BOOK_FILE}")
        WORDS = ["Error: Book file not found!"] #Provide a placeholder.
    except Exception as e:
        print(f"Error reading file: {e}")
        WORDS = ["Error reading file!"]

@app.route('/hello_world')
def hello():
    return "Привет, мир!"

@app.route('/cars')
def show_cars():
    return ", ".join(cars)

@app.route('/cats')
def random_cat():
    return random.choice(cats)

@app.route('/get_time/now')
def time_now():
    return f"Точное время и дата: {datetime.now().strftime(time_format)}"

@app.route('/get_time/future')
def time_future():
    return f"Время через час: {(datetime.now() + timedelta(hours=1)).strftime(time_format)}"

@app.route('/get_random_word')
def get_random_word():
    global WORDS
    if not WORDS:
        return "Word list is empty (check the book file path/encoding)!" #Error Handling!
    return random.choice(WORDS)

@app.route('/counter')
def counter():
    global visits
    visits += 1
    return f"Страница открыта {visits} раз"

if __name__ == "__main__":
    load_words()
    app.run(debug=True)