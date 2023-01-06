#  The total number of videos to be clipped


# Folder to save the videos clipped ( It must be a folder that doesn't exist
# , and it's where you get you clipped videos) and also it is used as the downloaded file_name
folder_and_file_name = "tappp"

# Note adding the path there must be a trailing slash to ignore the first slash
# This is only use if you are using Local as the video location
video_path = "C:\\Users\\Codertjay\\PycharmProjects\\fiverr_projects\\edit_video\\youtube_videos\\newtoy.mp4"

# The YouTube Link if the user chooses YouTube
youtube_link = "https://www.youtube.com/watch?v=QYURIo3dWPk"

# List of clip in time format this could be as many as you need it according ly
# Example you need to clip one
# clip_time_and_video_file = [
#     ["00:00:01", "00:00:10",video_path],
#     ["00:00:01", "00:00:10",youtube_link],
#     ]
# And if you don't want to merge you change the

clip_time_and_video_file_or_link = [
    ["00:00:01", "00:00:10", video_path],
    ["00:00:01", "00:00:10", youtube_link],
    ["00:00:01", "00:00:10", video_path],
]

# Could be True or False if you want to merge all videos
merge_video = True
