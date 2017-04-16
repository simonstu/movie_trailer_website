import webbrowser

class Movie():
    """class for a movie"""
    def __init__(self, movie_title, movie_storyline, poster_img, trailer_youtube):
        """a movie needs a title, storyline, url for the poster and url to a trailer on youtube"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """open a browser to show the trailer"""
        webbrowser.open(self.trailer_youtube_url)