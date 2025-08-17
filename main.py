import cv2
import os

def extract_frames(video_path, output_folder, image_format="png"):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    os.makedirs(output_folder, exist_ok=True)

    frame_count = 0
    success = True

    while success:
        success, frame = cap.read()
        if success:
            filename = os.path.join(output_folder, f"frame_{frame_count:05d}.{image_format}")
            cv2.imwrite(filename, frame)
            frame_count += 1
            print(f"Saved {filename}")

    cap.release()
    print(f"Done! Extracted {frame_count} frames to '{output_folder}'.")

# Example usage
if __name__ == "__main__":
    extract_frames("[VIDEO_NAME].mp4", "frames_output", image_format="png")
