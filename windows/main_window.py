import tkinter as tk
import threading
import logging

from tkinter import filedialog
from tkinter.ttk import Progressbar, Style
from PIL import ImageTk, Image
from pathlib import Path
from pytube import YouTube

from windows.custom_windows import TextInfo


class MainWindow:
    def __init__(self):

        # Silencing the pytube logger
        logging.getLogger("pytube.__main__").setLevel(logging.WARNING)

        self.window = tk.Tk()
        self.x = 600
        self.y = 300
        self.window.geometry(f"{self.x}x{self.y}")
        self.window.title("KIH Tata Downloader v.1.0.0")
        self.window.configure(bg="white")

        # Namespace placeholders
        self.video = None
        self.stream = None
        self.directory = None

        # Styles
        style = Style()
        style.theme_use('clam')
        style.configure("white.Horizontal.TProgressbar", foreground='white', background='white')

        # # Logo
        logo_path = Path(__file__).resolve().parent.parent / 'graphics' / 'logo-final-120.png'
        img = ImageTk.PhotoImage(Image.open(logo_path))
        self.panel = tk.Label(self.window, image=img)
        self.panel.place(x=self.x * 0.5, y=self.y * 0.025, anchor="n")

        # Link entry section
        self.entry_y = self.y * 0.55
        self.link_entry_label = tk.Label(text="Link do YouYube: ", bg="white")
        self.link_entry_label.place(x=self.x * 0.04, y=self.entry_y, anchor="w")

        self.link_entry = tk.Entry(self.window, fg="darkred", bg="white", width=int(self.x * 0.105))
        self.link_entry.place(x=self.x * 0.215, y=self.entry_y, anchor="w")

        self.button_download = tk.Button(command=self.download_video, text="Ściągnij", bg="white", fg="black")
        self.button_download.place(x=self.x * 0.95, y=self.entry_y, anchor="e")

        # Progress Bar and Progress Label, it will appear while downloading
        self.progress_bar = Progressbar(self.window, orient="horizontal", maximum=100, length=382, mode='determinate',
                                        style="white.Horizontal.TProgressbar")
        self.progress_percent = tk.Label(self.window, text="0%", fg="darkred", bg="white", font=("Agency FB", 15))

        self.contact = tk.Label(text="Tatalski, jak coś nie działa to dawaj znać.\n Będziemy naprawiać i rozwijać :)",
                                bg="white", fg="black")
        self.contact.place(x=self.x * 0.5, y=self.y * 0.85, anchor="center")

        self.window.mainloop()

    def download_video(self):

        self.directory = self.change_download_destination()
        logging.info(f"Download directory: {self.directory}")

        yt_link = self.link_entry.get()
        logging.info(f"Link: {yt_link}")

        self.video = YouTube(yt_link)
        logging.info("Connection to the youtube movie established\n")
        logging.info(f"Title: {self.video.title}")

        self.stream = self.video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        logging.info(f"Filesize: {round(self.stream.filesize / 1024**2, 1)}MB")

        self.create_progressbar()

        threading.Thread(target=self.video.register_on_progress_callback(self.update_progressbar)).start()
        threading.Thread(target=self.download_start).start()

    def download_start(self):
        self.stream.download(self.directory)

    def change_download_destination(self):
        root = tk.Tk()
        root.withdraw()
        directory = filedialog.askdirectory()
        return directory

    def create_progressbar(self):
        self.progress_bar.place(x=self.x * 0.215, y=self.y * 0.65, anchor="w")

        self.progress_percent.place(x=self.x * 0.9, y=self.y * 0.65, anchor="center")

    def remove_progressbar(self):
        self.progress_bar.place_forget()
        self.progress_percent.place_forget()

    def create_info_popup(self, title, text):
        root = tk.Tk()
        root.withdraw()
        TextInfo(root, title, text=text)

    def update_progressbar(self, stream=None, chunk=None, remaining=None):
        # Gets the percentage of the file that has been downloaded.
        percent = int(100 - (100 * (remaining / self.stream.filesize)))
        if percent < 100:
            self.progress_percent.config(text=str(percent) + "%")
            self.progress_bar['value'] = percent
        else:
            self.remove_progressbar()
            logging.info("Movie downloaded")
