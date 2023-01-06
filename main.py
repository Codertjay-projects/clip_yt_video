from moviepy.video.io.VideoFileClip import VideoFileClip

from clip_videos import clip_multiple_videos_and_merge
from custom_questions import ask_use_local_video_or_youtube
from custom_variable import folder_name
from moviepy_helper import create_folder


def edit_video():
    # It returns the full path to the video
    # And it asks the user to choose between local video or YouTube link
    video_file = ask_use_local_video_or_youtube()
    # loading video to get duration
    clip = VideoFileClip(video_file)
    # getting duration of the video
    video_duration = float(clip.duration)

    print("The video duration in Seconds: ", video_duration)
    # Let's create the folder where we need to save the video created
    create_folder(folder_name=folder_name)
    # Clip of merge videos
    clip_multiple_videos_and_merge(video_duration=video_duration, video_file=video_file)


##############
# Calling the edit video function
edit_video()
##############
