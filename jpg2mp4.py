import cv2
import os
from datetime import date

today = date.today()
cwd = os.getcwd()
print(cwd)

# Set the path to the folder containing the JPG images
image_folder = r'C:\Users\wen-hao.wu\Desktop\Bayer_Converter\outputs'

# Set the name of the output video file
video_name = os.path.join(cwd, 'output', 'testvid' + str(today) + '.mp4')


# Set the frame rate of the video (in frames per second)
frame_rate = 1.0

# Get a list of all the jpg images in the folder
image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.jpg')]

# Sort the image files alphabetically
image_files.sort()

# Read the first image to get its size
img = cv2.imread(image_files[0])
height, width, channels = img.shape

# Create the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(video_name, fourcc, frame_rate, (width, height))

# Loop over the image files and add each one to the video
for image_file in image_files:
    # Read the image
    img = cv2.imread(image_file)
    # Add the image to the video
    for i in range(int(frame_rate*2)):
        video_writer.write(img)
        print("processing...")

# Release the video writer
video_writer.release()
print("DONE!")