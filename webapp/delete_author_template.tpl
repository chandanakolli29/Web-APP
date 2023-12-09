delete_author_template = '''
<!doctype html>
<html>
    <head>
        <title>Delete Author</title>
    </head>
    <body>
        <h2>Delete Author</h2>
        <p>Are you sure you want to delete {{ author_info['author_name'] }}?</p>
        <form action="/delete-author" method="post">
            <input type="hidden" name="author_id" value="{{ author_info['author_id'] }}">
            <input type="submit" value="Delete">
        </form>
    </body>
</html>
'''