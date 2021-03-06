import csv
import math

from operator import itemgetter

movies = {}
users = {}


def main():
    # Create Movie objects for each item in u.item file
    with open('u.item', encoding='latin_1') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            # movie id | movie title | release date | video release date | IMDb URL | genres
            movies[row[0]] = Movie(id=row[0],
                                   name=row[1],
                                   release_date=row[2],
                                   video_release_date=row[3],
                                   imdb_url=row[4],
                                   genres=row[5])

    # Create user objects for each item in u.user file
    with open('u.user') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            users[row[0]] = User(id=row[0],
                                 age=row[1],
                                 gender=row[2],
                                 occupation=row[3])

    # Add ratings to movie and user objects
    with open('u.data') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            users[row[0]].ratings[row[1]] = {'rating': row[2], 'timestamp': row[3]}
            movies[row[1]].ratings[row[0]] = {'rating': row[2], 'timestamp': row[3]}

    # Calculate average rating for each movie and user
    for movie in movies.values():
        movie.avg_rating = Ratings.avg_rating(movie.ratings)

    for user in users.values():
        user.avg_rating = Ratings.avg_rating(user.ratings)

    Interface.program_loop()


class Movie:

    def __init__(self, **kwargs):
        self.id = ''
        self.name = ''
        self.release_date = ''
        self.video_release_date = ''
        self.imdb_url = ''
        self.genres = []
        self.ratings = {}
        self.avg_rating = ''
        self.similar_users = []

        for k, v in kwargs.items():
            setattr(self, k, v)

    def update_ratings(self, inp):
        self.ratings = inp


class Interface:

    def program_loop():
        while True:
            print("Welcome to Movie Database")
            user_input = 0
            while user_input not in ('1', '2', '3'):
                user_input = input('1. See top movies.\n2. Search by user.\n3. Quit.\n>>> ')
            if user_input == '1':
                Interface.show_top_movies()
            elif user_input == '2':
                Interface.user_movies()
            else:
                exit()

    def show_top_movies():
        num_of_movies = input('How many movies should be displayed? ')
        top_movies = Ratings.get_top_x(num_of_movies, 150)
        num = 1
        for movie in enumerate(top_movies):
            print(movie[0] + 1, ": ", movie[1][2])
            num += 1

    def user_movies():
        user_num = input('Please enter a user number: ')
        user_choice = 0
        while user_choice not in ('1', '2'):
            user_choice = input('1. Top rated, popular movies, you havn\'t seen.\n2. Movie recommentations.\n>>> ')
        if user_choice == '1':
            user_movies = Ratings.get_user_top_x(user_num, 10, 150)
            for movie in enumerate(user_movies):
                print(movie[0] + 1, ": ", movie[1][2])
        else:
            user_movies = Ratings.recommended_movies(user_num)
            num = 1
            for movie in user_movies:
                print(num, ": ", movies[movie].name)
                num += 1

    def print_movie_list(user_movies):
        for movie in enumerate(movies):
            print(movie[0] + 1, ": ", movie[1][2])


class User:

    def __init__(self, **kwargs):
        self.id = ''
        self.name = ''
        self.first_name = ''
        self.middle_name = ''
        self.last_name = ''
        self.email = ''
        self.age = ''
        self.gender = ''
        self.occupation = ''
        self.zip = ''
        self.ratings = {}
        self.avg_rating = ''

        for k, v in kwargs.items():
            setattr(self, k, v)


class Ratings:

    def avg_rating(ratings):
        all_ratings = [int(x.get('rating')) for x in ratings.values()]
        return "%.2f" % float(sum(all_ratings)/len(all_ratings))

    def get_top_x(x, min_ratings):
        top_list = []
        for movie in movies.values():
            if (len(movie.ratings)) > int(min_ratings):
                top_list.append([movie.id, movie.avg_rating, movie.name])
        return sorted(top_list, reverse=True,  key=lambda y: y[1])[:int(x)]

    def get_user_top_x(id, x, min_ratings):
        watched = users[id].ratings.keys()
        top_x = [[movies[k].id, movies[k].avg_rating, movies[k].name] for k in movies.keys() if k not in watched and len(movies[k].ratings) > int(min_ratings)]
        return sorted(top_x, reverse=True, key=lambda y: y[1])[:int(x)]

    def euclidean_distance(usr1, usr2):
        """
        Given two user ids, give the Euclidean distance between their
        movie ratings on a scale of 0 to 1. 1 means the two lists are
        identical.
        """
        usr1_movies = [movie_id for movie_id in users[usr1].ratings.keys()]
        usr2_movies = [movie_id for movie_id in users[usr2].ratings.keys()]
        same_movies = [movie_id for movie_id in usr1_movies if movie_id in usr2_movies]
        users_ratings = {}
        for movie_id in same_movies:
            user1_ratings = users[usr1].ratings.get(movie_id).get('rating')
            user2_ratings = users[usr2].ratings.get(movie_id).get('rating')
            users_ratings[movie_id] = {'user_1': user1_ratings, 'user_2': user2_ratings}

        user1_ratings = []
        user2_ratings = []

        for movie_id in users_ratings.values():
            user1_ratings.append(int(movie_id['user_1']))
            user2_ratings.append(int(movie_id['user_2']))

        # Guard against empty lists.
        if len(user1_ratings) is 0:
            return 0

        # Note that this is the same as vector subtraction.
        diffs = [user1_ratings[idx] - user2_ratings[idx] for idx in range(len(user1_ratings))]
        squares = [diff ** 2 for diff in diffs]
        sum_of_squares = sum(squares)

        return 1 / (1 + math.sqrt(sum_of_squares))

    def similiar_users(usr1):
        """Returns a list of lists with [userid, similarity]"""
        ratings = []
        for usr2 in users.keys():
            ratings.append([usr2, Ratings.euclidean_distance(users[usr1].id, usr2)])
        return sorted(ratings, key=itemgetter(1), reverse=True)[:1000]

    def recommended_movies(usr1):
        similiar_users = Ratings.similiar_users(usr1)
        movies_seen = [x for x in users[usr1].ratings.keys()]
        suggested_movies = {}

        for user in similiar_users:
            user_movies = list(users[user[0]].ratings.keys())
            for movie in user_movies:
                if movie not in movies_seen:
                    user_movie_rating = users[user[0]].ratings[movie]['rating']
                    user_movie_weight = user[1] * float(user_movie_rating)
                    if movie in suggested_movies:
                        suggested_movies[movie] += user_movie_weight
                    else:
                        suggested_movies[movie] = user_movie_weight

        sorted_suggestions = []
        for k, v in suggested_movies.items():
            sorted_suggestions.append([k, v])

        top_10_suggested = (sorted(sorted_suggestions, key=itemgetter(1), reverse=True)[:10])
        return [x[0] for x in top_10_suggested]


if __name__ == '__main__':
    main()
