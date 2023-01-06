from clip_videos import clip_multiple_videos_and_merge
from custom_variable import folder_and_file_name
from moviepy_helper import create_folder


def edit_video():
    create_folder(folder_name=folder_and_file_name)
    # Clip of merge videos
    clip_multiple_videos_and_merge()


##############
# Calling the edit video function
edit_video()
##############
