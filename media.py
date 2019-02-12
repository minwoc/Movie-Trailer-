import webbrowser

class Movie():
    ''' This is a class that provides a way to store movie related informationself.
    We can think of class Movie as a blueprint that stores all the functionality for this code.
    Here, we have method to open up the url through that of object webbrowser.open.'''

    '''The summary line for a class docstring should fit on one line.

    This class also has instance attributes under the function init.
    Attributes may be documented inline with the attribute's declaration (see __init__ method below).

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    '''


    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        ''' It is important to remember that def __init__ helps to create memory in spaceself.
        On top, we are creating instance variables here.
        The variables movie_title, movie_storyline, poster_image, trailer_youtube store information we made
        from entertainment_center.py.
        It helps to minimize rewriting the code, and coveniently supports
        to create instance methods.
        '''

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
            '''This is an instance method. We can use instance variable inside of this method and class to
        open up the URL by utilizing webbrowser.open function.'''
