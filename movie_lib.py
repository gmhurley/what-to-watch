import csv


class Movie:

    def __init__(self, **kwargs):
        self.id = ''
        self.name = ''
        self.release_date = ''
        self.video_release_date = ''
        self.genres = []
        self.ratings = {}
        self.avg_rating = 0

        for k, v in kwargs.items():
            setattr(self, k, v)


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
        self.avg_rating = 0

        for k, v in kwargs.items():
            setattr(self, k, v)


movie_dict = {}
users = {}

# Create Movie objects for each item in u.item file
with open('u.item', encoding='latin_1') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        movie_dict[row[0]] = Movie(id=row[0],
                                   name=row[1],
                                   release_date=row[2],
                                   video_release_date=row[3],
                                   genres=row[4])

# Create user objects for each item in u.user file
with open('u.user') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        users[row[0]] = User(id=row[0],
                             age=row[1],
                             gender=row[2],
                             occupation=row[3])

