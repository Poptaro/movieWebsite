import webbrowser

class Movie():
    """Here, we have a template-like storage for movies listed in movieFile.py"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #This function allows direct input in the movieFile variables
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
#this function will allow user(s) to click on a movie poster and have the trailer pop up
    def show_trailer(self):
        """
        This shows trailer
        :return:
        """
        webbrowser.open(self.trailer_youtube_url)

