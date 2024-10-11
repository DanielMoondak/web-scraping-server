from flask import Flask, render_template
from scrape_script import scrape_books, scrape_categories

app = Flask(__scrape__)

@app.route('/')
def home():
    categories = scrape_categories()  # Obtener las categorías
    books = scrape_books()  # Obtener los libros
    return render_template('index.html', categories=categories, books=books)

if __scrape__ == '__main__':
    app.run(debug=True)
