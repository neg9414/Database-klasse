import random

class artworks:
    def __init__ (self, artist: str, painting: str, year: int, genre: str, beskrivelse: str):
        self.artist = artist
        self.painting = painting
        self.year = year
        self.genre = genre
        self.beskrivelse = beskrivelse

    def __str__ (self):
        return f' artist: {self.artist} har lavet {self.painting} som har genren {self.genre} i {self.year}. {self.beskrivelse}'