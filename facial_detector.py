import cv2

# Load the pre-trained Haar Cascade classifier for face detection
# Ensure you have the 'haarcascade_frontalface_default.xml' file in the same directory as this script.
face_cap = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Use the webcam for live video feed
video_cap = cv2.VideoCapture(0)

# Set screen dimensions for full-screen display
screen_width = 1920
screen_height = 1080

# Create a named window and set it to full screen
cv2.namedWindow("video_live", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("video_live", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    # Capture frame-by-frame from the webcam
    ret, video_data = video_cap.read()
    if not ret:  # Break the loop if no frame is captured
        break

    # Convert the frame to grayscale for face detection
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw rectangles around detected faces in the original frame
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (255, 255, 0), 2)

    # Resize the output frame to maintain aspect ratio for full screen
    output_frame = cv2.resize(video_data, (screen_width, screen_height))

    # Display the video frame with rectangles around faces
    cv2.imshow("video_live", output_frame)

    # Exit the loop when the 'a' key is pressed
    if cv2.waitKey(10) == ord("a"):
        break

# Release the video capture object and close all OpenCV windows
video_cap.release()
cv2.destroyAllWindows()
