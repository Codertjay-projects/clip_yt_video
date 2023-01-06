import os.path

from moviepy.video.io.VideoFileClip import VideoFileClip

from custom_questions import get_start_and_end_time
from custom_variable import clip_time_and_video_file_or_link, merge_video, folder_and_file_name
from moviepy_helper import merge_all_videos, extract_video_clip
from youtube_downloader import Download


def clip_multiple_videos_and_merge():
    ##################################################################
    """ To get how many times video should be clipped and also the start and end time"""
    # the clip_times is in the format [[start,end],[start,end],[start,end]]
    # base on the number of clip we need to create
    video_clipped_list = []

    for index in range(len(clip_time_and_video_file_or_link)):
        # Clip a single video
        video_clipped = clip_single_video(
            start_time=clip_time_and_video_file_or_link[index][0],
            end_time=clip_time_and_video_file_or_link[index][1],
            video_path_or_link=clip_time_and_video_file_or_link[index][2],
            index=index
        )
        video_clipped_list.append(VideoFileClip(video_clipped))
    ###########################################################################
    """Merge Video if the merge is True"""
    if merge_video:
        """ Merge videos"""
        if len(video_clipped_list) > 1:
            merge_all_videos(video_clipped_list, folder_and_file_name)
        print("Video Successfully Merged")


def clip_single_video(start_time, end_time, video_path_or_link, index):
    # get_start_and_end_time returns [start_time_in_sec,end_time_in_sec]
    # loading video to get duration
    # Check if it's a link or download
    if video_path_or_link.startswith("https://www.youtube.com/"):
        video_path = Download(link=video_path_or_link, filename=folder_and_file_name)
    elif os.path.exists(video_path_or_link):
        # Check if it's a path
        video_path = video_path_or_link
    else:
        print("The video file or link is not correct")
        exit()

    clip = VideoFileClip(video_path)
    # getting duration of the video
    video_duration = float(clip.duration)

    start_and_end_time = get_start_and_end_time(
        start_time=start_time,
        end_time=end_time,
        video_duration=video_duration)
    # file_path is where we want to save the new clipped video
    file_path = f"{folder_and_file_name}/{folder_and_file_name}{index}.mp4"
    # Replace empty space
    file_path.replace(" ", "")
    video_clipped = extract_video_clip(file_name=video_path, time_start=start_and_end_time[0],
                                       time_end=start_and_end_time[1],
                                       file_path=file_path)
    print(f"Successfully Clipped {index}")
    return video_clipped
