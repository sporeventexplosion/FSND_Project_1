from fresh_tomatoes import open_movies_page

class Movie():
    def __init__(self, title, description, poster_image_url, trailer_youtube_url):
        self.title = title
        self.description = description
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

a = Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "http://www.youtube.com/watch?v=vwyZH85NQC4")

b = []
b.append(a)

open_movies_page(b)
