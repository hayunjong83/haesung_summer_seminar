import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("cctv2.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("object_blurring_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize object blurrer object
blurrer = solutions.ObjectBlurrer(
    show=True,  # display the output
    model="yolo11s.pt",  # model for object blurring i.e. yolo11m.pt
    # line_width=2,  # width of bounding box.
    classes=[0],  # count specific classes i.e, person and car with COCO pretrained model.
    # blur_ratio=0.5,  # adjust percentage of blur intensity, the value in range 0.1 - 1.0
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = blurrer(im0)

    # print(results")  # access the output

    # video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows