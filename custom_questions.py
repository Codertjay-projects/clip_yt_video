import os
import re

import questionary

from custom_variable import video_location, youtube_link, video_path, downloaded_file_name
from youtube_downloader import Download

# defining colors
CBLUE = "\33[34m"
CEND = "\33[0m"
CRED = "\33[31m"


def ask_use_local_video_or_youtube():
    try:
        # It returns the path to the video file
        # Ask the user questions
        print("\n")

        if video_location == "YouTube":
            # then the user wants to use local video
            filename = downloaded_file_name

            video_file = Download(link=youtube_link, filename=filename.replace(" ", "_"))
            # Return the file path
            return video_file
        elif video_location == "Local":
            print("\n")
            # The path in which the video is located in the user machine
            video_file = video_path
            if not os.path.exists(video_file):
                print("\n")
                print(CRED + "The path to this video does not exist and if you feel exist try removing "
                             "space from video file " + CEND)
                print("\n")
                # It aks the user the same question again
                print("Please put in the correct file location")
                exit()
            return video_file
        else:
            exit()
    except:
        print(CRED + "Please input the right params" + CEND)
        exit()


# converting time to seconds
def time_to_sec(t):
    h, m, s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s


def check_time_format(clip_time):
    # regex to validate HH:MM:SS format
    match_timestamp = re.compile(r'^[0-9]{2}:[0-9]{2}:[0-9]{2}$', re.IGNORECASE)
    if re.match(match_timestamp, clip_time):
        return clip_time
    else:
        print(CRED + "Timestamps mis formatted! Insert HH:MM:SS (Hours, Minutes, Seconds)" + CEND)
        exit()


# checking video timestamps both for pattern and inconsistency
def check_timestamps(start_time, end_time, video_length):
    start_time_in_sec = time_to_sec(start_time)
    end_time_in_sec = time_to_sec(end_time)
    if time_to_sec(
            "00:00:00") <= start_time_in_sec < end_time_in_sec <= video_length:
        return True
    elif video_length < end_time_in_sec:
        print(CRED + "> End time is larger than video length! \n \n" + CEND)
        return False
    else:
        print("\n")
        print(CRED + "> Timestamps invalid! \n \n" + CEND)
        exit()
        return False


def get_start_and_end_time(start_time, end_time, video_duration):
    # Returns the start an end time in list format if no error

    # We range through the video_counts to aks time for each

    start_time = check_time_format(start_time)
    end_time = check_time_format(end_time)
    # check the time the user set if valid
    if check_timestamps(start_time, end_time, video_duration):
        # Convert both time to seconds
        start_time = time_to_sec(start_time)
        end_time = time_to_sec(end_time)
        return [start_time, end_time]
    else:
        print("\n")
        print(CRED + f"An error occurred not able to process question for the number {1} clip" + CEND)
        exit()
