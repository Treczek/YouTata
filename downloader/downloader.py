import logging
import pytube

from pytube.exceptions import RegexMatchError as RegexMatchError


class Downloader:
    def __init__(self, youtube_link):

        logging.getLogger("pytube.__main__").setLevel(logging.WARNING)

        self._youtube_link = youtube_link
        logging.info(f"Link: {youtube_link}")
        self.ys = None

        try:
            self.yt = pytube.YouTube(self._youtube_link)
        except RegexMatchError:
            logging.warning("Niepoprawny link. Spróbuj jeszcze raz.")
            raise ValueError

    def get_description(self):

        youtube_stats = dict(title=self.yt.title, views=self.yt.views, length=self.yt.length,
                             rating=self.yt.rating, description=self.yt.description)
        return youtube_stats

    def start(self, directory):

        self.ys = self.yt.streams.filter(file_extension="mp4").first()
        logging.info(f"Size: {round(self.ys.filesize / 1024**2,1)} MB")
        self.ys.download(directory)
        logging.info("Film ściągnięty")
