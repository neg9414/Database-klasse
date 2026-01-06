from database import Database

db = Database()

# Søgning på en bestemt person
term = "marie van"
print(db.search(term))

# Opret/create nyt maleri til min tabel
db.insert(
    id=78,
    artist="marie van",
    painting="bad",
    year=2023,
    genre="Impressionism",
    image="noimage.jpg",
    beskrivelse="Et af maries mest berømte værker."
)

# Henter et bestemt maleri
print(db.load())

# Vis alle malerier
print(db.load_all()) 
