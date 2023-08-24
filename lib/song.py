class Song:
    # Class variables to store song data
    all_songs = []
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
    count = 0

    def __init__(self, name, artist, genre):
        # Instance variables
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class variables
        Song.all_songs.append(self)
        Song.genres.add(self.genre)
        Song.artists.add(self.artist)
        Song.count += 1

        # Update genre count
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

        # Update artist count
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

    @classmethod
    def song_count(cls):
        return cls.count


# Example usage of the Song class
if __name__ == "__main__":
    Song("99 Problems", "Jay Z", "Rap")
    Song("Halo", "Beyonce", "Pop")
    Song("Smells Like Teen Spirit", "Nirvana", "Rock")

    out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
    print(f"Total song count: {Song.song_count()}")

    print(f"Genres: {', '.join(Song.genres)}")
    print(f"Artists: {', '.join(Song.artists)}")
    print(f"Genre Count: {Song.genre_count}")
    print(f"Artist Count: {Song.artist_count}")
