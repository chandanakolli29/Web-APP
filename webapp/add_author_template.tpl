add_author_template='''
<!-- Define template for adding an author -->
<!doctype html>
<html>
    <head>
        <title>Add Author</title>
    </head>
    <body>
        <h2>Add Author</h2>
        <form action="/add-author" method="post">
            Author Name: <input type="text" name="author_name" required><br>
            <input type="submit" value="Add Author">
        </form>
    </body>
</html>
'''
