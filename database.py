import sqlite3
from artworks import Artwork


class Database:
    def __init__(self, db_name="artworks.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS artworks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, artist TEXT, year INTEGER)""")
        self.conn.commit()

    # Min create til at lave en nu række
    def save(self, artwork: Artwork):
        self.cursor.execute(
            "INSERT INTO artworks (title, artist, year) VALUES (?, ?, ?)",
            (artwork.title, artwork.artist, artwork.year)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    # Her kan jeg hente og læse information fra et maleri
    def load(self, id):
        self.cursor.execute("SELECT * FROM artworks WHERE id = ?", (id,))
        row = self.cursor.fetchone()
        if row:
            return Artwork(row[0], row[1], row[2], row[3])
        return None

    # Henter alle mine rækker
    def load_all(self):
        self.cursor.execute("SELECT * FROM artworks")
        rows = self.cursor.fetchall()
        return [Artwork(r[0], r[1], r[2], r[3]) for r in rows]

    # Sletter en række 
    def delete(self, id):
        self.cursor.execute("DELETE FROM artworks WHERE id = ?", (id,))
        self.conn.commit()
