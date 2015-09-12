import csv

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

        for k, v in kwargs.items():
            setattr(self, k, v)

    def update_ratings(self, inp):
        self.ratings = inp


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

    def get_top_x(x):
        top_list = []
        for movie in movies.values():
            top_list.append([movie.avg_rating, movie.name])
        return sorted(top_list, reverse=True)[:int(x)]

    def get_user_top_x(id, x):
        watched = users[id].ratings.keys()
        top_x = [[movies[k].avg_rating, movies[k].name] for k in movies.keys() if k not in watched]
        return sorted(top_x, reverse=True)[:int(x)]


if __name__ == '__main__':
    main()
