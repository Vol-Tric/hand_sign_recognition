# import cv2

# # Try camera index 0
# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Camera not found or cannot be opened.")
# else:
#     print("Camera is working fine.")


# import cv2

# cap = cv2.VideoCapture(0)  # Try with index 0 first

# if not cap.isOpened():
#     print("Error: Unable to access the camera")
# else:
#     # Proceed with camera operations
#     ret, frame = cap.read()
#     if ret:
#         cv2.imshow("Frame", frame)
#     else:
#         print("Error: Unable to read from the camera")

# cap.release()
# cv2.destroyAllWindows()


import cv2

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Unable to access the camera")
else:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly, ret is True
        if not ret:
            print("Failed to grab frame")
            break

        # Display the frame
        cv2.imshow('Live Video Feed', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
