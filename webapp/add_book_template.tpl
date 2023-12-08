add_book_template = '''
<!doctype html>
<html>
    <head>
        <title>Add Book</title>
    </head>
    <body>
        <h2>Add Book</h2>
        <form action="/add-book" method="post">
            Book Name: <input type="text" name="book_name" required><br>
            Book Description: <input type="text" name="book_description" required><br>
            Author ID: <input type="text" name="author_id" required><br>
            <input type="submit" value="Add Book">
        </form>
    </body>
</html>
'''