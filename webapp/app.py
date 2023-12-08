from bottle import Bottle, template, request, redirect
from mongita import MongitaClientDisk

app = Bottle()
client = MongitaClientDisk()  # Use in-memory storage for simplicity
db = client['library']

# Sample authors data
authors_data = [
    {"author_id": 1, "author_name": "Rabindranath Tagore"},
    {"author_id": 2, "author_name": "George Orwell"},
    {"author_id": 3, "author_name": "Charles Dickens"},
    {"author_id": 4, "author_name": "Mahatma Gandhi "},
    {"author_id": 5, "author_name": "Arundhati Roy"},
]

# Sample books data
books_data = [
    {"book_name": "Gitanjali", "book_description": "collection of poems", "author_id": 1},
    {"book_name": "Animal Farm", "book_description": "Russian Revolution's rhetoric and history", "author_id": 2},
    {"book_name": "Oliver Twist", "book_description": "somber tale of corruption", "author_id": 3},
    {"book_name": "My Experiments with the Truth", "book_description": "autobiography that covers his life", "author_id": 4},
    {"book_name": "God of Small Things", "book_description": "story of fraternal twins", "author_id": 5}
]

# Insert data into authors and books collections
db.authors.insert_many(authors_data)
db.books.insert_many(books_data)

@app.route('/')
def index():
    return template(index_template)

@app.route('/search', method='POST')
def search():
    author_id = request.forms.get('author_id')

    try:
        # Perform a basic query to find books for the given author ID
        result = list(db.books.find({'author_id': int(author_id)}))

        # Fetch author information separately
        author_info = db.authors.find_one({'author_id': int(author_id)})

        if not author_info:
            return "Author not found."

        if not result:
            return "No books found for the given author ID."

        # Pass the result and author information to the template
        return template(result_template, result=result, author_info=author_info)

    except Exception as e:
        return f"Error: {e}"
# Route for displaying the form to add a book
@app.route('/add-book')
def add_book_form():
    return template(add_book_template)

# Route for handling the addition of a book
@app.route('/add-book', method='POST')
def add_book():
    try:
        book_name = request.forms.get('book_name')
        book_description = request.forms.get('book_description')
        author_id = int(request.forms.get('author_id'))

        # Perform the actual addition of the book to the database
        db.books.insert_one({
            "book_name": book_name,
            "book_description": book_description,
            "author_id": author_id
        })

        return f"Book '{book_name}' added successfully."

    except Exception as e:
        return f"Error adding book: {e}"

# Route for displaying the form to add an author
@app.route('/add-author')
def add_author_form():
    return template(add_author_template)

# Route for handling the addition of an author
@app.route('/add-author', method='POST')
def add_author():
    try:
        author_name = request.forms.get('author_name')

        # Perform the actual addition of the author to the database
        db.authors.insert_one({
            "author_name": author_name
        })

        return f"Author '{author_name}' added successfully."

    except Exception as e:
        return f"Error adding author: {e}"

@app.route('/update-author/<author_id:int>')
def update_author_form(author_id):
    author_info = db.authors.find_one({'author_id': author_id})
    return template(update_author_template, author_info=author_info)

@app.route('/update-author', method='POST')
def update_author():
    author_id = request.forms.get('author_id')
    new_author_name = request.forms.get('author_name')

    # Update the author's name based on author_id
    db.authors.update_one({'author_id': int(author_id)}, {'$set': {'author_name': new_author_name}})
    
    # Redirect to the search page or any other appropriate page
    redirect('/')

@app.route('/delete-author/<author_id:int>')
def delete_author_form(author_id):
    author_info = db.authors.find_one({'author_id': author_id})
    return template(delete_author_template, author_info=author_info)

@app.route('/delete-author', method='POST')
def delete_author():
    author_id = request.forms.get('author_id')

    # Delete the author based on author_id
    db.authors.delete_one({'author_id': int(author_id)})

    # Redirect to the search page or any other appropriate page
    redirect('/')
    
if __name__ == '__main__':
    app.run(host='localhost', port=8080)
