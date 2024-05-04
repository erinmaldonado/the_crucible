import subprocess
import os

def process_video(video_path):
    file_path = os.path.join('/data', 'raw_data', video_path)
    print(f"Processing...: {file_path}")
    # Example of using subprocess to call an external command
    # subprocess.run(["your_command_here", video_path])

if __name__ == "__main__":
    process_video(video_path)
