from random import shuffle

class MP3Playlist:
    def __init__(self):
        self.playlist = []

    def load_playlist(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                track = line.strip()
                if track.endswith(".mp3"):
                    self.playlist.append(track)

    def display_playlist(self):
        if not self.playlist:
            print("Playlist is empty.")
        else:
            print("Loading Playlist:")
            for index, track in enumerate(self.playlist, start=1):
                print(f"{index}. {track}")

    def add_track(self, track_name, artiste, album, duration, genre, year):
        if track_name.endswith(".mp3"):
            self.playlist.append(track_name, artiste, duration)
            print(f"'{track_name}' has been added to the playlist.")

    def remove_track(self, track_index):
        if track_index < 0 <= len(self.playlist):
            removed_track = self.playlist.pop(track_index - 1)
            print(f"'{removed_track}' has been removed from the playlist.")
        else:
            print("Invalid track index.")

    def save_playlist(self, filename):
        New_Playlist = open(filename + ".txt", 'w')
        for track in self.playlist:
            filename.write(f"{track.name}, {track.artiste}, {track.album}, {track.duration}, {track.genre}, {track.year}")

    def shuffle_playlist(self):
        shuffle(self.playlist)
        print("Playlist shuffled.")

    def count_tracks(self):
        print(f"Playlist has {len(self.playlist)} loaded")

    def total_duration(self):
        total_seconds = 0
        for track in self.playlist:
            track_duration = track.duration(60, 120, 240)
            

    def clear_playlist(self):
        self.playlist = []
        print("Playlist cleared.")

    def is_empty(self):
        return "Playlist is empty" if len(self.playlist) == 0 else "Playlist is not empty"


playlist = MP3Playlist()
playlist.load_playlist("Playlist.txt")
playlist.display_playlist()
playlist.enqueue_track("new_track1.mp3")
playlist.enqueue_track("new_track2.mp3")
playlist.display_playlist()
playlist.enqueue_track("new_track1.mp3")
playlist.enqueue_track("new_track2.mp3")
playlist.enqueue_track("new_track3.mp3")
playlist.remove_track(3)
playlist.display_playlist()
playlist.shuffle_playlist()
print(playlist.is_empty())
playlist.add_track()
playlist.display_playlist()
playlist.count_tracks()
playlist.remove_track(2)
playlist.save_playlist("new_playlist.txt")
playlist.clear_playlist()
print(playlist.is_empty)


