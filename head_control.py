import cv2
import numpy as np

class HeadController:
    def __init__(self):  # Corrected constructor
        self.cap = cv2.VideoCapture(0)  # Use the webcam
        
    def get_head_movement(self):
        _, frame = self.cap.read()
        frame = cv2.flip(frame, 1)  # Flip frame to act as a mirror
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Load the pre-trained frontal face detector from OpenCV
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        movement_direction = None

        if len(faces) > 0:
            # Sort faces by area (w * h) to find the largest face
            faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
            (x, y, w, h) = faces[0]  # Pick the largest face

            # Draw a rectangle around the largest face (for debugging)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Get the center of the face for movement detection
            center_x = x + w // 2
            center_y = y + h // 2

            # Detect movement direction based on y-axis and x-axis positions
            if center_y < frame.shape[0] // 2 - 20:
                movement_direction = 'up'  # Tilt head up
            elif center_y > frame.shape[0] // 2 + 20:
                movement_direction = 'down'  # Tilt head down
            elif center_x < frame.shape[1] // 2 - 20:
                movement_direction = 'left'  # Tilt head left
            elif center_x > frame.shape[1] // 2 + 20:
                movement_direction = 'right'  # Tilt head right
            else:
                movement_direction = 'neutral'  # No movement

        cv2.imshow('Head Control', frame)  # Display the webcam feed (for debugging)
        return movement_direction

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

# For testing purposes
if __name__ == "__main__":
    controller = HeadController()
    while True:
        direction = controller.get_head_movement()
        print("Direction: ", direction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    controller.release()


