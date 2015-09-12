import csv
import math

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

    # Find similar tastes
    # for user in users.values():
    #     print(user.id)

    # Each list is made up of ratings for movies they've both seen in the same order


    print(Ratings.euclidean_distance('22', '23'))


    # user_1_ratings = [users['22'].ratings.get(x).get('rating') for x in same_movies]
    # print(user_1_ratings)

    # print(users['22'].ratings.items())
    # print(user_1, "\n")
    # print(user_2, "\n")
    # print(same_movies, "\n")


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
    pass


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
                top_list.append([movie.avg_rating, movie.name])
        return sorted(top_list, reverse=True)[:int(x)]

    def get_user_top_x(id, x, min_ratings):
        watched = users[id].ratings.keys()
        top_x = [[movies[k].avg_rating, movies[k].name] for k in movies.keys() if k not in watched and len(movies[k].ratings) > int(min_ratings)]
        return sorted(top_x, reverse=True)[:int(x)]

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

if __name__ == '__main__':
    main()
