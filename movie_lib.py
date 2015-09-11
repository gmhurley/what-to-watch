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
        self.age = ''
        self.gender = ''
        self.occupation = ''
        self.zip = ''
        self.ratings = {}
        self.avg_rating = {}

        for k, v in kwargs.items():
            setattr(self, k, v)
