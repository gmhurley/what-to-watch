from movie_lib import *

# Movies for testing
# toy_story = Movie(id='1', name='Toy Story')

movies = {'1': Movie(id='1', name='Toy Story',
                     ratings={'1': {'timestamp': '884641983', 'rating': '4'},
                              '2': {'timestamp': '884130542', 'rating': '4'}}),
          '2': Movie(id='2', name='Top Gun',
                     ratings={'1': {'timestamp': '884641842', 'rating': '5'},
                              '2': {'timestamp': '882150192', 'rating': '1'}}),
          '3': Movie(id='3', name='Pretty Women',
                     ratings={'1': {'timestamp': '884641681', 'rating': '2'},
                              '2': {'timestamp': '884641842', 'rating': '4'}}),
          '4': Movie(id='4', name='Seven',
                     ratings={'1': {'timestamp': '884641983', 'rating': '2'}}),
          '5': Movie(id='4', name='Richard III',
                     ratings={}),
          '6': Movie(id='4', name='Braveheart',
                     ratings={}),
          '7': Movie(id='4', name='Twelve Monkeys',
                     ratings={}),
          '8': Movie(id='4', name='Copycat',
                     ratings={}),
          '9': Movie(id='4', name='GoldenEye',
                     ratings={'1': {'timestamp': '884641983', 'rating': '5'}}),
          '10': Movie(id='4', name='Desperado',
                      ratings={})}

glenn_ratings = {'1': {'timestamp': '884641983', 'rating': '4'},
                 '2': {'timestamp': '884641842', 'rating': '5'},
                 '3': {'timestamp': '884641681', 'rating': '2'},
                 '4': {'timestamp': '884641983', 'rating': '2'},
                 '9': {'timestamp': '884641983', 'rating': '5'}}

rose_ratings = {'1': {'rating': '4', 'timestamp': '884642981'},
                '2': {'rating': '1', 'timestamp': '884641743'},
                '3': {'rating': '4', 'timestamp': '884641842'}}

# Users for testing
glenn = User(id='1', name='Glenn', age=32, gender='M', ratings=glenn_ratings)
rose = User(id='2', name='Rose', age=31, gender='F', ratings=rose_ratings)


def test_movie_creation():
    assert movies['1'].id == '1'
    assert movies['1'].name == 'Toy Story'


def test_user_creation():
    assert glenn.id == '1'
    assert glenn.name == 'Glenn'
    assert glenn.age == 32
    assert glenn.gender == 'M'


def test_avg_rating():
    glenn.avg_rating = Ratings.avg_rating(glenn.ratings)
    rose.avg_rating = Ratings.avg_rating(rose.ratings)
    movies['1'].avg_rating = Ratings.avg_rating(movies['1'].ratings)
    movies['2'].avg_rating = Ratings.avg_rating(movies['2'].ratings)

    assert glenn.avg_rating == '3.60'
    assert rose.avg_rating == '3.00'
    assert movies['1'].avg_rating == '4.00'
    assert movies['2'].avg_rating == '3.00'



def test_top_x():
    pass
