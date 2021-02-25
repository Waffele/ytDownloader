from pytube import YouTube


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def yt_download(link):
    yt = YouTube(link)
    # Title of video
    print("Title: ", yt.title)
    # Number of views of video
    print("Number of views: ", yt.views)
    # Length of the video
    print("Length of video: ", yt.length, " seconds")
    # Description of video
    print("Description: ", yt.description)
    # Rating
    print("Ratings: ", yt.rating)
    ys = yt.streams.get_highest_resolution()
    ys.download()


if __name__ == '__main__':
    print_hi('PyCharm')
    yt_download(input("insert link: "))

