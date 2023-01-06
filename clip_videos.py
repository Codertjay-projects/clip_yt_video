from moviepy.video.io.VideoFileClip import VideoFileClip

from custom_questions import ask_count_clipped, get_start_and_end_time
from moviepy_helper import merge_all_videos, extract_video_clip


def clip_multiple_videos_and_merge(video_duration, video_file, folder_name, merge=False):
    ##################################################################
    """ To get how many times video should be clipped and also the start and end time"""
    # we ask the user how many times would he or she want the video to be clipped
    video_counts = ask_count_clipped()
    # if the user index is one I  Clip videos into multiple files
    clip_times_list = []
    # the clip_times is in the format [[start,end],[start,end],[start,end]]
    # base on the number of clip we need to create
    for index in range(video_counts):
        index += 1
        print("\n")
        # get_start_and_end_time returns [start_time_in_sec,end_time_in_sec]
        print(f"Input the start and end time for clip number {index} \n")
        start_and_end_time = get_start_and_end_time(video_duration)
        # append it to our list
        clip_times_list.append(start_and_end_time)
    #########################################################################
    """Clip the videos into multiple file"""
    # loop through the time we want to clip

    count = 0
    video_clipped_list = []
    for item in clip_times_list:
        # start clipping
        file_path = f"{folder_name}/{folder_name}{count}.mp4"
        # Replace empty space
        file_path.replace(" ","")
        video_clipped = extract_video_clip(file_name=video_file, time_start=item[0], time_end=item[1],
                                           file_path=file_path)
        count += 1
        # Append the video location to the list of videos clipped
        video_clipped_list.append(VideoFileClip(video_clipped))
        print(f"Successfully Clipped {count}")
    ###########################################################################
    """Merge Video if the merge is True"""
    if merge == True:
        """ Merge videos"""
        merge_all_videos(video_clipped_list, folder_name)
        print("Video Successfully Merged")


def clip_single_video(video_duration, video_file, folder_name):
    # Clip Single video out
    start_and_end_time = get_start_and_end_time(video_duration)
    file_path = f"{folder_name}/{folder_name}.mp4"
    video_clipped = extract_video_clip(file_name=video_file, time_start=start_and_end_time[0],
                                       time_end=start_and_end_time[1],
                                       file_path=file_path)
    print("Clipped video is located at, ", f"{folder_name}/{folder_name}.mp4")
    print("Video Successfully Clipped")
