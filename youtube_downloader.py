from pytube import YouTube

CRED = "\33[31m"
CEND = "\33[0m"


def Download(link, filename):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        print("#################")
        video_file = youtubeObject.download(filename=f"{filename}.mp4", output_path="youtube_videos")
        print("##################################")
        print("Download is completed successfully")
        return video_file
    except Exception as a:
        print("\n")
        print(a)
        print(CRED + "An error has occurred" + CEND)
        exit()
