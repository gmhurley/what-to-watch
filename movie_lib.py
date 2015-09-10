import csv

MOVIE_DICT = {}
with open('movie_data.txt', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        MOVIE_DICT[row[0]] = {'Name': row[1],
                              'Release_Date': row[2],
                              'Video_Date': row[3],
                              'IMDB': row[4],
                              'Genres': row[5:]}


class Movie:

    def __init__(self, **kwargs):
        self.movie_id = ''
        self.name = ''
        self.release_date = ''
        self.video_release_date = ''
        self.genres = []

    def movie_by_id(inp):
        return MOVIE_DICT[inp]['Name']


class User:
    pass


class Ratings:
    pass
