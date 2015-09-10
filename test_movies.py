from movie_lib import *


def test_all_movie_ratings_by_movie_id():
    pass


def test_avg_movie_ratings():
    pass


def test_movie_name_by_id():
    assert Movie.movie_by_id('1') == 'Toy Story (1995)'
    assert Movie.movie_by_id('1') != 'GoldenEye (1995)'
    assert Movie.movie_by_id('50') == 'Star Wars (1977)'
    assert Movie.movie_by_id('50') != 'I.Q. (1994)'


def test_all_user_ratings():
    pass
