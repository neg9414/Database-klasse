import random

class Artwork:
    def __init__(self, id=None, title=None, artist=None, year=None):
        self.id = id
        self.title = title
        self.artist = artist
        self.year = year

    def __str__(self):
        return f"{self.id}: {self.title} af {self.artist} i ({self.year})"