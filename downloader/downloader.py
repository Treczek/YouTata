import logging
import pytube

from pytube.exceptions import RegexMatchError as RegexMatchError


class Downloader:
    def __init__(self, youtube_link):

        logging.getLogger("pytube.__main__").setLevel(logging.WARNING)

        self._youtube_link = youtube_link
        logging.info(f"\nLink: {youtube_link}")

        try:
            self.yt = pytube.YouTube(self._youtube_link)
        except RegexMatchError:
            logging.warning("Niepoprawny link. Spróbuj jeszcze raz.")
            raise ValueError

    def print_description(self):
        logging.info(f"Title:  {self.yt.title}")
        logging.info(f"Number of views: {self.yt.views}")
        logging.info(f"Length: {self.yt.length} seconds")
        logging.info(f"Ratings: {self.yt.rating}")

    def start(self, directory):
        ys = self.yt.streams.get_highest_resolution()
        ys.download(directory)
        logging.info("Film ściągnięty")
