import re

# defining colors
CBLUE = "\33[34m"
CEND = "\33[0m"
CRED = "\33[31m"


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
