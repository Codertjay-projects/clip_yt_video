#  The total number of videos to be clipped


# Folder to save the videos clipped ( It must be a folder that doesn't exist
# , and it's where you get you clipped videos)
folder_name = "my_folder"

# List of clip in time format
clip_time_list_time_format = [
    ["00:00:01", "00:00:10"],
    ["00:00:01", "00:00:10"],
    ["00:00:01", "00:00:10"],

]

# Could be True or False
merge_video = True

# YouTube Or Local
# Note its capfirst
video_location = "Local"
# Note adding the path there must be a trailing slash to ignore the first slash
video_path = "C:\\Users\\Codertjay\\PycharmProjects\\fiverr_projects\\edit_video\\youtube_videos\\newtoy.mp4"

# The YouTube Link if the user chooses YouTube
youtube_link = "https://www.youtube.com/watch?v=QYURIo3dWPk"
# The name you are willing to give the video file after download
# ( Please make sure the file name does not exist
# try adding a new file name )
# I used the folder name right now, but you can change it
downloaded_file_name = folder_name
