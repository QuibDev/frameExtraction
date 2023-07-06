import cv2
import os

def extract_frames(video_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Get total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Extract frames
    for frame_num in range(total_frames):
        # Read the frame
        success, frame = video.read()

        if not success:
            break

        # Save the frame as an image file
        frame_path = os.path.join(output_folder, f"frame_{frame_num}.jpg")
        cv2.imwrite(frame_path, frame)

    # Release the video file
    video.release()

# Path to the input video file
video_path = "path_to_your_video.avi"

# Path to the output folder
output_folder = "frames"

# Call the function to extract frames
extract_frames(video_path, output_folder)
