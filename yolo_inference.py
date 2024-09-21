from ultralytics import YOLO

# Download and load the model
model = YOLO('best.pt')  # replace 'yolov8n.pt' with the desired model version
results=model.predict('input_videos/08fd33_4.mp4',save=True)
print(results[0])
print('aaaaaaaaaaaaaaaaaaaaaaaaaaa')
for box in results[0].boxes:
    print(box)