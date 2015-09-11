from movie_lib import *

# Movies for testing
toy_story = Movie(id='1', name='Toy Story')

# Users for testing
glenn = User(id='1', name='Glenn', age=32, gender='M')


def test_movie_creation():
    assert toy_story.id == '1'
    assert toy_story.name == 'Toy Story'


def test_user_creation():
    assert glenn.id == '1'
    assert glenn.name == 'Glenn'
    assert glenn.age == 32
    assert glenn.gender == 'M'
