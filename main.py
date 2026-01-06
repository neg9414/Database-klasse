from artworks import Artwork
from database import Database

db = Database()

# Gemmer en ny række
a1 = Artwork(title="Stjerne Nat", artist="Van Gogh", year=1889)
a1.id = db.save(a1)
print("Saved:", a1)

# Henter en række til at aflæse
fetched = db.load(a1.id)
print("Loaded:", fetched)

# Hent alt
all_artworks = db.load_all()
for art in all_artworks:
    print("Alle:", art)
