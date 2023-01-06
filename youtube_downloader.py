import os.path

from pytube import YouTube

CRED = "\33[31m"
CEND = "\33[0m"


def Download(link, filename):
    """Returns the full path to the downloaded video"""

    try:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        print("#################")
        video_file = youtubeObject.download(filename=f"{filename}.mp4", output_path="youtube_videos")
        print("##################################")
        print("Download is completed successfully")
        if not os.path.exists(video_file):
            print(CRED + "An error has occurred downloading video . Please make sure you have an active internet"
                         " and also the link is a valid one" + CEND)
            exit()
        return video_file
    except:
        print("\n")
        print(CRED + "An error has occurred downloading video . Please make sure you have an active internet"
                     " and also the link is a valid one" + CEND)
        exit()
