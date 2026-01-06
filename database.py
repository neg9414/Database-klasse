import sqlite3

DB_FILE = "artworks.db"

class Database:
    def __init__(self):
        self._create_table()

    def _connect(self):
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        return conn

    def _execute(self, query, params=()):
        conn = self._connect()
        try:
            conn.execute(query, params)
            conn.commit()
        finally:
            conn.close()

    def _run_query(self, query, params=()):
        conn = self._connect()
        try:
            cur = conn.execute(query, params)
            rows = cur.fetchall()
        finally:
            conn.close()
        return {"rows": [dict(row) for row in rows]}
    
    
    def _create_table(self):
        query = """CREATE TABLE IF NOT EXISTS artworks ( id INTEGER PRIMARY KEY, artist TEXT NOT NULL, painting TEXT NOT NULL, year INTEGER, genre TEXT, image TEXT, beskrivelse TEXT )"""
        self._execute(query)

    def search(self, term):
        query = """SELECT * FROM artworks WHERE artist LIKE ? OR painting LIKE ? OR genre LIKE ?"""
        return self._run_query(query, (f"%{term}%", f"%{term}%", f"%{term}%"))

    def load(self, artwork_id):
        query = "SELECT * FROM artworks WHERE id = ?"
        return self._run_query(query, (artwork_id,))

    def load_all(self):
        query = "SELECT * FROM artworks"
        return self._run_query(query)

    def insert(self, id, artist, painting, year, genre, image, beskrivelse):
        query = """INSERT INTO artworks (id, artist, painting, year, genre, image, beskrivelse) VALUES (?, ?, ?, ?, ?, ?, ?) """
        self._execute(query, (id, artist, painting, year, genre, image, beskrivelse))

    def deleted (self):
        query = "DELETED * FROM artworks WHERE id = ?" 
        return self._run_query(query)

    def update (self):
        query = "UPDATE * FROM artworks (id, artist, painting, year, genre, image, beskrivelse) VALUES (?, ?, ?, ?, ?, ?, ?) """
        return self._run_query(query)