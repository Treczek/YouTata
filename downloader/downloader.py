import pytube


class Downloader:
    def __init__(self, youtube_link):
        self._youtube_link = youtube_link

        print("\nLink", youtube_link)
        self.yt = pytube.YouTube(self._youtube_link)

    def print_description(self):

        print("Title: ", self.yt.title)
        print("Number of views: ", self.yt.views)
        print("Length: ", self.yt.length, "seconds")
        print("Ratings: ", self.yt.rating)

    def start(self, directory):
        ys = self.yt.streams.get_highest_resolution()
        ys.download(directory)
        print("Film ściągnięty.")
