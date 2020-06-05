class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


louvre = Painting(input(), input(), input())

print(f'"{louvre.title}" by {louvre.artist} ({louvre.year}) hangs in the {Painting.museum}.')
