from moviepy.video.io.VideoFileClip import VideoFileClip

from clip_videos import clip_multiple_videos_and_merge, clip_single_video
from custom_questions import ask_user_wants, ask_use_local_video_or_youtube, ask_folder_name


def edit_video():
    # It returns the full path to the video
    # And it asks the user to choose between local video or YouTube link
    video_file = ask_use_local_video_or_youtube()
    # loading video to get duration
    clip = VideoFileClip(video_file)
    # getting duration of the video
    video_duration = float(clip.duration)

    print("The video duration in Seconds: ", video_duration)

    # Ask the user if he or she just wants to clip one or multiple videos
    user_wants_index = ask_user_wants()

    # Ask the user where to save the video file
    folder_name = ask_folder_name()

    if user_wants_index == 1:
        # Clip multiple videos
        clip_multiple_videos_and_merge(video_duration=video_duration, video_file=video_file, folder_name=folder_name)
    elif user_wants_index == 2:
        # Clip a Single Video
        clip_single_video(video_duration=video_duration, video_file=video_file, folder_name=folder_name)
    elif user_wants_index == 3:
        # Clip multiple videos  and also merge
        clip_multiple_videos_and_merge(video_duration=video_duration, video_file=video_file, folder_name=folder_name,
                                       merge=True)


##############
# Calling the edit video function
edit_video()
##############
