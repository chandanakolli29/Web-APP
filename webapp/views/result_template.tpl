result_template = '''
<!doctype html>
<html>
    <head>
        <title>Search Results</title>
    </head>
    <body>
        <h2>Search Results</h2>
        % if author_info:
            <p>Author Name: {{ author_info['author_name'] }}</p>
            <p><a href="/update-author/{{ author_info['author_id'] }}">Update Author</a></p>
            <p><a href="/delete-author/{{ author_info['author_id'] }}">Delete Author</a></p>
        % else:
            <p>Author not found.</p>
        % end
        % if result:
            <table border="1">
                <tr>
                    <th>Book Name</th>
                    <th>Book Description</th>
                    <th>Actions</th>
                </tr>
                % for item in result:
                    <tr>
                        <td>{{ item['book_name'] }}</td>
                        <td>{{ item['book_description'] }}</td>
                        <td>
                            <a href="/update-book/{{ item['_id'] }}">Update</a>
                            <a href="/delete-book/{{ item['_id'] }}">Delete</a>
                        </td>
                    </tr>
                % end
            </table>
        % else:
            <p>No books found for the given author ID.</p>
        % end
    </body>
</html>
'''