      
import argparse
from src.models.import_video import process_video

def main():
    parser = argparse.ArgumentParser(description="Process video files.")
   
    # Process video file
    parser.add_argument('--process', type=str, required=True, help='Video file to process')

    
    
    args = parser.parse_args()
    
    if args.process == 'twitch_nft_demo.mp4':
        print("The specified file is 'twitch_nft_demo.mp4'. Starting...")
        process_video(args.process)
        # end
        print("Process complete...")
    else:
        print("Processing other video file:", args.process)
        
    if args.

if __name__ == "__main__":
    main()