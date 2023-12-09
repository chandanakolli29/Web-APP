update_author_template = '''
<!doctype html>
<html>
    <head>
        <title>Update Author Information</title>
    </head>
    <body>
        <h2>Update Author Information</h2>
        <form action="/update-author" method="post">
            <input type="hidden" name="author_id" value="{{ author_info['author_id'] }}">
            Author Name: <input type="text" name="author_name" value="{{ author_info['author_name'] }}" required>
            <input type="submit" value="Update">
        </form>
    </body>
</html>
'''