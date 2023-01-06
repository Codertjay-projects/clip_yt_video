from moviepy.video.io.VideoFileClip import VideoFileClip

from custom_questions import get_start_and_end_time
from custom_variable import clip_time_list_time_format, merge_video, folder_name
from moviepy_helper import merge_all_videos, extract_video_clip


def clip_multiple_videos_and_merge(video_duration, video_file):
    ##################################################################
    """ To get how many times video should be clipped and also the start and end time"""
    # if the user index is one I  Clip videos into multiple files
    clip_times_list_in_sec = []
    # the clip_times is in the format [[start,end],[start,end],[start,end]]
    # base on the number of clip we need to create
    for index in range(len(clip_time_list_time_format)):
        # get_start_and_end_time returns [start_time_in_sec,end_time_in_sec]
        start_and_end_time = get_start_and_end_time(
            start_time=clip_time_list_time_format[index][0],
            end_time=clip_time_list_time_format[index][1],
            video_duration=video_duration)
        # append it to our list
        clip_times_list_in_sec.append(start_and_end_time)
    #########################################################################
    """Clip the videos into multiple file"""
    # loop through the time we want to clip

    count = 0
    video_clipped_list = []
    for item in clip_times_list_in_sec:
        # start clipping
        file_path = f"{folder_name}/{folder_name}{count}.mp4"
        # Replace empty space
        file_path.replace(" ", "")
        video_clipped = extract_video_clip(file_name=video_file, time_start=item[0], time_end=item[1],
                                           file_path=file_path)
        count += 1
        # Append the video location to the list of videos clipped
        video_clipped_list.append(VideoFileClip(video_clipped))
        print(f"Successfully Clipped {count}")
    ###########################################################################
    """Merge Video if the merge is True"""
    if merge_video:
        """ Merge videos"""
        merge_all_videos(video_clipped_list, folder_name)
        print("Video Successfully Merged")
