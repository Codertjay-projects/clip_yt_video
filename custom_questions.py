import os
import re

import questionary

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
        user_wants = questionary.select(
            "What do you want to do?",
            choices=[
                "1) Use youtube link. ",
                "2) Use local video. ",
            ]).ask()
        user_wants_index = int(user_wants[0])
        if user_wants_index == 1:
            # then the user wants to use local video
            filename = input("Please input filename? ")
            youtube_link = input("Please input youtube link? ")

            video_file = Download(link=youtube_link, filename=filename.replace(" ", "_"))
            # Return the file path
            return video_file
        elif user_wants_index == 2:
            print("\n")
            # The user chose the video located on his or machine
            video_file = questionary.path("What's the path to the video?").ask()
            if not os.path.exists(video_file):
                print("\n")
                print(CRED + "The path to this video does not exist and if you feel exist try removing "
                             "space from video file " + CEND)
                print("\n")
                # It aks the user the same question again
                print("Please put in the correct file location")
                return ask_use_local_video_or_youtube()
            return video_file
        else:
            exit()
    except:
        print(CRED + "Please input the right params" + CEND)
        exit()


def ask_user_wants() -> int:
    # It returns an integer
    # Ask the user questions
    user_wants = questionary.select(
        "What do you want to do?",
        choices=[
            "1) Clip videos into multiple files. ",
            "2) Clip a single video. ",
            "3) Clip videos into multiple files and also merge. ",
        ]).ask()
    # Get the first character which is used as the index
    user_wants_index = user_wants[0]
    return int(user_wants_index)


def ask_count_clipped():
    # returns the clip count
    try:
        clips_count = int(input("How many clips do you want to create? "))
        if clips_count <= 0:
            print("\n")
            print(CRED + "Integer need to be positive" + CEND)
            print("\n")

            return ask_count_clipped()
        return clips_count
    except ValueError:
        print('Please enter an integer.')
        exit()
        return ask_count_clipped


# converting time to seconds
def time_to_sec(t):
    h, m, s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s


def ask_time_to_clip(question):
    clip_time = input(f"Input {question} time in this format HH:MM:SS (Hours, Minutes, Seconds): ")
    # regex to validate HH:MM:SS format
    match_timestamp = re.compile(r'^[0-9]{2}:[0-9]{2}:[0-9]{2}$', re.IGNORECASE)
    if re.match(match_timestamp, clip_time):
        return clip_time
    else:

        print(CRED + "Timestamps mis formatted! Insert HH:MM:SS (Hours, Minutes, Seconds)" + CEND)

        # Ask the user the same question
        return ask_time_to_clip(question)


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


def ask_folder_name():
    # Ask the user what folder could be used to save the file
    target_name = input("What name would you like to give the folder? ")
    target_name.replace(" ", "_")
    # Create the directory using the target name if it doesn't exist
    if not os.path.exists(target_name):
        os.mkdir(target_name)
        return target_name
    else:
        print("\n")
        print(CRED + "> Folder name already exists !\n \n" + CEND)
        return ask_folder_name()


def get_start_and_end_time(video_duration):
    # Returns the start an end time in list format if no error

    # We range through the video_counts to aks time for each

    start_time = ask_time_to_clip("start")
    end_time = ask_time_to_clip("end")
    # check the time the user set if valid
    if check_timestamps(start_time, end_time, video_duration):
        # Convert both time to seconds
        start_time = time_to_sec(start_time)
        end_time = time_to_sec(end_time)
        return [start_time, end_time]
    else:
        print("\n")
        print(CRED + f"An error occurred not able to process question for the number {1} clip" + CEND)
        print("Question has been restart \n ")
        return get_start_and_end_time(video_duration)
