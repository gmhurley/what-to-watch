import csv

MOVIE_DICT = {}
RATINGS = {}
USERS = {}

with open('movie_data.txt', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        MOVIE_DICT[row[0]] = {'Name': row[1],
                              'Release_Date': row[2],
                              'Video_Date': row[3],
                              'IMDB': row[4],
                              'Genres': row[5:]}

with open('data.txt') as datafile:
    reader = csv.reader(datafile, delimiter=' ', skipinitialspace=True)
    key_num = 1
    for row in reader:
        RATINGS[key_num] = {'user_id': row[0],
                            'movie_id': row[1],
                            'rating': row[2],
                            'timestamp': row[3]}
        key_num += 1

with open('users.txt') as userfile:
    reader = csv.reader(userfile, delimiter='|')
    for row in reader:
        USERS[row[0]] = {'age': row[1],
                         'gender': row[2],
                         'occupation': row[3],
                         'zip': row[4]}


class Movie:

    def __init__(self, **kwargs):
        self.movie_id = ''
        self.name = ''
        self.release_date = ''
        self.video_release_date = ''
        self.genres = []

    def movie_by_id(self, inp):
        return MOVIE_DICT[inp]['Name']

    def ratings_by_id(self, inp):
        return [v['rating'] for k, v in RATINGS.items() if (v['movie_id']) == inp]

    def avg_rating(self, inp):
        ratings = [int(x) for x in self.ratings_by_id(inp)]
        return "%.2f" % float(sum(ratings)/len(ratings))


class User:

    def all_user_ratings(self, inp):
        return [v['rating'] for k, v in RATINGS.items() if (v['user_id']) == inp]

    def watched(self, user):
        return [v['movie_id'] for k, v in RATINGS.items() if (v['user_id'] == user)]


class Ratings:

    def top_x(self, num):
        top_lst = []
        for k, v in MOVIE_DICT.items():
            top_lst.append([Movie().avg_rating(k), v['Name']])
        return sorted(top_lst, reverse=True)[:num]

    def top_x_not_watched(self, num, user):
        watched = User().watched(user)
        top_lst = [[Movie().avg_rating(k), v['Name']] for k, v in MOVIE_DICT.items() if k not in watched]
        return sorted(top_lst, reverse=True)[:num]

print(Ratings().top_x(10))
print(Ratings().top_x_not_watched(10, '745'))
