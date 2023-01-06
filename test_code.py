import subprocess

# Create a list of input video paths
input_videos = ["./masr/masr_0.mp4", "./masr/masr_1.mp4"]

# Create the command to be run by FFmpeg
command = ["ffmpeg"]

# Add the input video arguments to the command
for input_video in input_videos:
    command.extend(["-i", input_video])

# Add the output video argument to the command
command.extend(["-c", "copy", "output.mp4"])

# Run the FFmpeg command
subprocess.run(command)