import tkinter as tk
from tkinter import messagebox

class MusicOrganizer:
    def __init__(self):
        self.collection = {}

    def add_song(self, title, artist, album, year):
        self.collection[title.lower()] = {
            'title': title,
            'artist': artist,
            'album': album,
            'year': year
        }

    def delete_song(self, title):
        return self.collection.pop(title.lower(), None)

    def search_song(self, title):
        return self.collection.get(title.lower())

    def get_all_songs(self):
        return list(self.collection.values())

# GUI Class
class MusicOrganizerGUI:
    def __init__(self, root):
        self.organizer = MusicOrganizer()
        self.root = root
        self.root.title("Music Organizer")

        # Labels and Entries
        tk.Label(root, text="Title").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(root, text="Artist").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(root, text="Album").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(root, text="Year").grid(row=3, column=0, padx=5, pady=5)

        self.title_entry = tk.Entry(root)
        self.artist_entry = tk.Entry(root)
        self.album_entry = tk.Entry(root)
        self.year_entry = tk.Entry(root)

        self.title_entry.grid(row=0, column=1)
        self.artist_entry.grid(row=1, column=1)
        self.album_entry.grid(row=2, column=1)
        self.year_entry.grid(row=3, column=1)

        # Buttons
        tk.Button(root, text="Add Song", command=self.add_song).grid(row=4, column=0, pady=10)
        tk.Button(root, text="View Collection", command=self.view_collection).grid(row=4, column=1)
        tk.Button(root, text="Search Song", command=self.search_song).grid(row=5, column=0)
        tk.Button(root, text="Delete Song", command=self.delete_song).grid(row=5, column=1)

        # Display area
        self.output_box = tk.Listbox(root, width=60)
        self.output_box.grid(row=6, column=0, columnspan=2, pady=10)

    def add_song(self):
        title = self.title_entry.get()
        artist = self.artist_entry.get()
        album = self.album_entry.get()
        year = self.year_entry.get()
        if title and artist and album and year:
            self.organizer.add_song(title, artist, album, year)
            messagebox.showinfo("Success", f"Added '{title}' to your collection.")
            self.clear_fields()
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")

    def view_collection(self):
        self.output_box.delete(0, tk.END)
        songs = self.organizer.get_all_songs()
        if songs:
            for song in songs:
                entry = f"{song['title']} - {song['artist']} ({song['album']}, {song['year']})"
                self.output_box.insert(tk.END, entry)
        else:
            self.output_box.insert(tk.END, "Your collection is empty.")

    def search_song(self):
        title = self.title_entry.get()
        song = self.organizer.search_song(title)
        self.output_box.delete(0, tk.END)
        if song:
            self.output_box.insert(tk.END, f"Found: {song['title']} - {song['artist']} ({song['album']}, {song['year']})")
        else:
            self.output_box.insert(tk.END, f"'{title}' not found in your collection.")

    def delete_song(self):
        title = self.title_entry.get()
        if self.organizer.delete_song(title):
            messagebox.showinfo("Deleted", f"'{title}' has been deleted.")
            self.view_collection()
        else:
            messagebox.showerror("Error", f"'{title}' not found in your collection.")

    def clear_fields(self):
        self.title_entry.delete(0, tk.END)
        self.artist_entry.delete(0, tk.END)
        self.album_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicOrganizerGUI(root)
    root.mainloop()
