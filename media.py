import json

from fresh_tomatoes import open_movies_page

MOVIES_FILENAME = 'movies.json'


class Movie():
    """
    An object representing single movie with a name, description, poster image
    url and the ID of its trailer on YouTube
    """

    def __init__(self, title, description, poster_image_url,
                 trailer_youtube_id):
        self.title = title
        self.description = description
        self.poster_image_url = poster_image_url
        self.trailer_youtube_id = trailer_youtube_id


def movie_from_dict(movie_dict):
    """Makes a Movie object from a dictionary"""

    return Movie(movie_dict['name'], movie_dict['description'],
                 movie_dict['poster_image_url'],
                 movie_dict['trailer_youtube_id'])


def open_from_json(filename):
    """Open the movie site with movies loaded from the JSON file filename"""

    movie_file = open(filename)
    movie_json = json.loads(movie_file.read())
    movie_file.close()
    movie_list = []

    # Make an object for each movie
    for movie in movie_json.get('movies', []):
        movie_list.append(movie_from_dict(movie))

    open_movies_page(movie_list)


open_from_json(MOVIES_FILENAME)
