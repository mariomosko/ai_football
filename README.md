
https://github.com/user-attachments/assets/627d0e3b-6461-403b-ab7d-6f6fcbf7294d
# ai_football

This Project provides a comprehensive tracking pipeline for football (soccer) analytics using deep learning and computer vision. It leverages YOLO models for object and pitch detection, and integrates tracking, annotation, and visualization utilities for sports analytics.

Key Features
Object Detection & Tracking:
Uses YOLO models to detect players, referees, and the ball in video frames. Tracks their positions across frames using ByteTrack.

Pitch Detection:
Detects the soccer pitch in each frame to enable spatial transformations and radar visualizations.

Position Interpolation:
Handles missing ball detections by interpolating positions for smoother tracking.

Annotation & Visualization:
Draws ellipses for players/referees, triangles for the ball, and overlays team ball control statistics. Generates a radar (top-down) view of player and ball positions on the pitch.

Team Ball Control Analysis:
Calculates and displays the percentage of ball possession for each team over time.

Modular Design:
Functions are organized for easy extension, including methods for detection, tracking, annotation, and radar rendering.



https://github.com/user-attachments/assets/b71b09eb-2527-40b7-b055-3f89ade61cdd


## Data Attribution

This project uses a video from the dataset:
- [DFL Bundesliga 460 MP4 Videos in 30Sec. + CSV ](https://www.kaggle.com/datasets/saberghaderi/-dfl-bundesliga-460-mp4-videos-in-30sec-csv?resource=download)

The original dataset is licensed under the [CC BY-SA 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/).

The video included here is a derivative work and is distributed under the terms of the same license.
