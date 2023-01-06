# add the video to this video clip
import os.path

from moviepy.editor import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip


def create_folder(folder_name):
    if os.path.exists(folder_name):
        print("Folder already exists please use another folder")
        exit()
    else:
        os.mkdir(folder_name)


def extract_video_clip(file_name, time_start, time_end, file_path):
    """ file_path: this is where i am saving the new video
    file_name: This is where the video is located
    """

    # Returns the location of the video created
    clip = VideoFileClip(file_name)
    # Specify the start and end times for the edited clip
    edited_clip = clip.subclip(time_start, time_end)
    # Save the edited clip to a new file
    edited_clip.write_videofile(file_path,
                                codec="h264",
                                bitrate="5000k",
                                threads=4,
                                preset="medium")
    return file_path


def merge_all_videos(video_clipped_list: list, folder_name):
    """
    This merges all videos in a list base on their order and the list contains
    instance of [VideoFileClip(file),VideoFileClip(file)]
    :return: None
    """
    print(video_clipped_list)
    print(video_clipped_list[0])
    # concatenating both the clips
    # Get the first clip frame per second
    fps = video_clipped_list[0].fps
    final = concatenate_videoclips(video_clipped_list, method="compose")
    # writing the video into a file / saving the combined video
    final.write_videofile(f"{folder_name}/merged_{folder_name}.mp4", codec="h264",
                          bitrate="5000k",
                          threads=4,
                          preset="medium", fps=fps)
