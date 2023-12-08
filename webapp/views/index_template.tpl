index_template = '''
<!doctype html>
<html>
    <head>
        <title>Author and Book Search</title>
    </head>
    <body>
        <h2>Search for Author and Book Information</h2>
        <form action="/search" method="post">
            Author ID: <input type="text" name="author_id" required>
            <input type="submit" value="Search">
        </form>
        <p><a href="/add-author">Add Author</a></p>
        <p><a href="/add-book">Add Book</a></p>
    </body>
</html>
'''