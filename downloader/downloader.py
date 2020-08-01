import pytube


class Downloader:
    def __init__(self, youtube_link):
        self._youtube_link = youtube_link
        print(youtube_link)
        self.yt = pytube.YouTube(self._youtube_link)

    def print_description(self):

        print("Title: ", self.yt.title)
        print("Number of views: ", self.yt.views)
        print("Length in minutes: ", self.yt.length, "seconds")
        print("Description: ", self.yt.description)
        print("Ratings: ", self.yt.rating)

    def start(self):
        ys = self.yt.streams.get_highest_resolution()
        ys.download()
