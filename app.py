from flask import Flask, render_template

app = Flask(__name__)

# list of books
books = [
    {"title" : "Dare to Lead", "author": "Brene Brown"},
    {"title" : "Move Fast and Fix Things", "author": "Frances Frei & Anne Morriss"},
    {"title" : "The Lean Startup", "author": "Eric Ries"},
    {"title" : "The Outsiders", "author": "William N. Thorndike Jr."},
    {"title" : "The Greater Good", "author": " Madeleine Shaw"},
    {"title" : "The 7 Habits of Highly Effective People", "author": "Stephen Covey"}
]
@app.route('/')
@app.route('/books')
def books_list():
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)