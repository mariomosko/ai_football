from utils import read_video, save_video
import cv2
import numpy as np
from trackers import Tracker

def main():
    # Read Video
    video_frames = read_video('input_videos/08fd33_4.mp4')


    # Initialize Tracker
    tracker = Tracker('best_Yolo_v5l_100ep.pt')

    tracks = tracker.get_object_tracks(video_frames)
    


    #save the cropped image of a player

   
    # Get object positions 
    tracker.add_position_to_tracks(tracks)
    
    # Draw output 
    ## Draw object Tracks
    output_video_frames=tracker.draw_annotations(video_frames,tracks)

    # Save video
    save_video(output_video_frames, 'output_videos/output_video.avi')
    print("aaaaaaaaaaaaaaaaaaaaaaaaa")

if __name__ == '__main__':
    main()