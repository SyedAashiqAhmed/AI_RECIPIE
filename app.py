from flask import Flask, render_template, request
from model import suggest_recipes
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recipes', methods=['POST'])
def get_recipes():
    available_ingredients = request.form['ingredients']
    recipes = suggest_recipes(available_ingredients)
    return render_template('index.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)
