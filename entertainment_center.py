import media
import fresh_tomatoes
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A marine on an aline planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=6ziBFh3V1aM")

school_of_rock = media.Movie(
    "School of Rock",
    "Using rock music to learn",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie(
    "ratatouille ",
    "Rat is chef in paris",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

Midnight_in_paris = media.Movie(
    "Midnight in paris",
    "Going back in time to meet authors",
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie(
    "School of Rock",
    "A really really reality show",
    "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")

'''Creating instances to use it in media class.
Here, the toy_story, avatar, school_of_rock, ratatouille,
Midnight_in_paris, and hunger_games
are all instances for class media.py.
It helps to carry necessary informations like title, description, and link to youtube url.  # NOQA
We can also think of it as we're creating parameters and information for class, where
class is thought of it as calling a function. '''

movies = [toy_story, avatar, school_of_rock, ratatouille, Midnight_in_paris, hunger_games]  # NOQA
fresh_tomatoes.open_movies_page(movies)
