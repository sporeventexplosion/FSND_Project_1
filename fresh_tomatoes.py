import webbrowser
import os
import cgi


def get_file_contents(filename):
    file_obj = open(filename)
    text = file_obj.read()
    file_obj.close()
    return text

page_main = get_file_contents('./template/main.html')
movie_tile = get_file_contents('./template/tile.html')


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        content += render_template(movie_tile,
                                   movie_title=movie.title,
                                   movie_description=movie.description,
                                   poster_image_url=movie.poster_image_url,
                                   trailer_youtube_id=movie.trailer_youtube_id)
    return content

# A very simple function for rendering a template string.
# Made to use double curly braces to not get 'tripped up' by CSS like .format
# Escape is optional so values are not double-escaped


def render_template(template, escape=True, **kwargs):

    for item in kwargs.items():
        # sanitize the values passed in
        if escape:
            value = cgi.escape(item[1])
        else:
            value = item[1]

        template = template.replace('{{' + item[0] + '}}', value)

    return template


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    rendered_tiles = create_movie_tiles_content(movies)

    # Replace the movie tiles placeholder generated content
    # Avoid escaping the already-escaped content from create_movie_tile_content
    rendered_content = render_template(page_main, escape=False,
                                       movie_tiles=rendered_tiles)

    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
