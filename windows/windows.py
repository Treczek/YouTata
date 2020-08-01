import logging
import tkinter as tk

from downloader import Downloader


class MainWindow:
    def __init__(self):

        window = tk.Tk()

        self.version = tk.Label(text="KIH-tata_downloader v.0.0.1")
        self.version.pack(side="top")

        self.create_space(1)

        self.link_entry_label = tk.Label(text="Link do YouYube:")
        self.link_entry_label.pack()

        self.link_entry = tk.Entry(window, fg="darkred", bg="white", width=50)
        self.link_entry.pack()

        self.button = tk.Button(
            # TODO dodać eksplorator
            command=self.get_yt_link,
            text="Ściągnij",
            width=12, height=1,
            bg="lightgray", fg="black",
        )
        self.button.pack()

        self.create_space(3)

        self.contact = tk.Label(text="Tatalski, jak coś nie działa to dawaj znać. Będziemy naprawiać i rozwijać :).")
        self.contact.pack()

        window.mainloop()

    def create_space(self, times):
        new_line = tk.Label(text="\n" * times)
        new_line.pack()

    def get_yt_link(self):
        yt_link = self.link_entry.get()
        self.download_video(yt_link)

    def download_video(self, yt_link):
        video = Downloader(yt_link)
        # video.print_description()
        video.start()

