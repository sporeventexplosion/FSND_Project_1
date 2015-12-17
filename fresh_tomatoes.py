import webbrowser
import os
import re

def get_file_contents(filename):
    file_obj = open(filename)
    text = file_obj.read()
    file_obj.close()
    return text

page_head = get_file_contents('./template/head.html')
page_body = get_file_contents('./template/body.html')
movie_tile = get_file_contents('./template/tile.html')

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        content += movie_tile.format(
            movie_title=movie.title,
            movie_description=movie.description,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=movie.trailer_youtube_id
        )
    return content

def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = page_head + page_body.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
