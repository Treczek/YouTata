import tkinter as tk
import logging

from tkinter import filedialog
from PIL import ImageTk, Image
from pathlib import Path

from downloader import Downloader


class MainWindow:
    def __init__(self):

        self.window = tk.Tk()
        self.x = 600
        self.y = 300
        self.window.geometry(f"{self.x}x{self.y}")
        self.window.title("KIH Tata Downloader v.0.5.0")
        self.window.configure(bg="white")

        logo_path = Path(__file__).resolve().parent.parent / 'graphics' / 'logo-final-120.png'
        img = ImageTk.PhotoImage(Image.open(logo_path))
        panel = tk.Label(self.window, image=img)
        panel.place(x=self.x*0.1, y=0.05)


        # Link entry section
        self.entry_y = self.y*0.55
        self.link_entry_label = tk.Label(text="Link do YouYube: ", bg="white")
        self.link_entry_label.place(x=self.x*0.04, y=self.entry_y, anchor="w")

        self.link_entry = tk.Entry(self.window, fg="darkred", bg="white", width=int(self.x*0.105))
        self.link_entry.place(x=self.x*0.215, y=self.entry_y, anchor="w")

        self.button_download = tk.Button(command=self.get_yt_link, text="Ściągnij", bg="white", fg="black")
        self.button_download.place(x=self.x*0.95, y=self.entry_y, anchor="e")

        self.contact = tk.Label(text="Tatalski, jak coś nie działa to dawaj znać.\n Będziemy naprawiać i rozwijać :).",
                                bg="white", fg="black")
        self.contact.place(x=self.x*0.5, y=self.y*0.75, anchor="center")

        self.button_download = tk.Button(command=lambda: logging.info("test"), text="test", bg="white", fg="black")
        self.button_download.place(x=self.x * 0.95, y=self.y*0.9, anchor="e")

        self.window.mainloop()

    def create_space(self, times):
        new_line = tk.Label(text="\n" * times)
        new_line.pack()

    def get_yt_link(self):
        yt_link = self.link_entry.get()
        self.download_video(yt_link)

    def download_video(self, yt_link):

        directory = self.change_download_destination()

        try:
            video = Downloader(yt_link)
        except ValueError:
            root = tk.Tk()
            root.withdraw()
            TextInfo(root, "Zły link", "Niepoprawny link")
            return None

        try:
            video.print_description()
            video.start(directory)
        except OSError:
            root = tk.Tk()
            root.withdraw()
            TextInfo(root, "Brak połączenia", "Internet jest niestety za słaby, spróbuj jeszcze raz.")

    def change_download_destination(self):
        root = tk.Tk()
        root.withdraw()
        return filedialog.askdirectory()


class TextInfo():
    def __init__(self, parent, window_title='window', textfield='a text field', label=None):

        self.top = tk.Toplevel(parent)
        self.parent = parent
        self.window_title = window_title
        self.textfield = textfield

        # set window title
        if window_title:
            self.top.title(window_title)

        # add label if given
        if label:
            tk.Label(self.top, text=window_title).grid(row=0)

        # create the text field
        self.textField = tk.Text(self.top, width=20, height=2, wrap=tk.NONE)
        if textfield:
            self.textField.insert(1.0, textfield)
        self.textField.grid(row=1)

        # create the ok button
        b = tk.Button(self.top, text="OK", command=self.ok)
        b.grid(row=2)

    def ok(self):
        self.top.destroy()
