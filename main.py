import cv2
import os

def extract_frames(video_path, output_folder, num_frames):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Get total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    print("\nDetected Video Footage at {} ...".format(video_path))

    # Calculate the step size to evenly extract frames
    step_size = max(total_frames // num_frames, 1)

    # Extract frames
    frame_num = 1
    while frame_num <= total_frames:
        # Set the frame position
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_num-1)

        # Read the frame
        success, frame = video.read()

        if not success:
            break

        # Save the frame as an image file
        frame_path = os.path.join(output_folder, f"frame_{frame_num}.jpg")
        cv2.imwrite(frame_path, frame)

        frame_num += step_size

    # Release the video file
    video.release()
    print("Frames saved in folder at {} ...".format(output_folder))

# Path to the main folder containing videos and subfolders
videos_folder = "C://Users/akash/Videos/1207"

# Number of frames to extract
num_frames = 10

# Recursive function to search for videos in subfolders
def search_videos(folder_path):
    # Iterate through all items in the folder
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isdir(item_path):
            # Recursively search videos in subfolders
            search_videos(item_path)
        elif item.endswith(".avi"):
            # Extract frames for the video
            video_name = os.path.splitext(item)[0]
            output_folder = os.path.join(folder_path, "Frames", video_name)
            extract_frames(item_path, output_folder, num_frames)


# Start searching videos in the main folder and subfolders
search_videos(videos_folder)
