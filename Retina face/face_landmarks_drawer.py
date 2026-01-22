import cv2
import numpy as np
import random

# ---------------------------
# Load image
# ---------------------------
image_path = r"..\Custom_Data\images\train\04876.png"
img = cv2.imread(image_path)

if img is None:
    raise ValueError("Image not found!")

# ---------------------------
# RetinaFace / DeepFace Output
# ---------------------------
data = {'face_1': {'score': np.float64(0.9993460774421692), 'facial_area': [np.int64(2854), np.int64(743), np.int64(4304), np.int64(2664)], 'landmarks': {'right_eye': [np.float32(3085.7524), np.float32(1487.0376)], 'left_eye': [np.float32(3640.7043), np.float32(1622.6619)], 'nose': [np.float32(3087.9558), np.float32(1862.9148)], 'mouth_right': [np.float32(2996.4597), np.float32(2151.1543)], 'mouth_left': [np.float32(3440.86), np.float32(2264.7563)]}}, 'face_2': {'score': np.float64(0.9983150959014893), 'facial_area': [np.int64(964), np.int64(1172), np.int64(2165), np.int64(2760)], 'landmarks': {'right_eye': [np.float32(1210.0765), np.float32(1939.7114)], 'left_eye': [np.float32(1743.3601), np.float32(1858.5626)], 'nose': [np.float32(1453.7206), np.float32(2209.6138)], 'mouth_right': [np.float32(1367.116), np.float32(2470.048)], 'mouth_left': [np.float32(1755.8785), np.float32(2398.2617)]}}}

# ---------------------------
# Draw all faces
# ---------------------------
for face_id, face_data in data.items():

    # Random color per face
    color = (255,0,0)# tuple(random.randint(50, 255) for _ in range(3))

    # Bounding box
    x1, y1, x2, y2 = map(int, face_data["facial_area"])
    cv2.rectangle(img, (x1, y1), (x2, y2), color, 5)

    # Face label
    cv2.putText(
        img,
        face_id,
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        color,
        3
    )

    # Landmarks
    for name, (x, y) in face_data["landmarks"].items():
        x, y = int(x), int(y)

        # Point
        cv2.circle(img, (x, y), 12, (0, 0, 255), -1)

        # Label
        cv2.putText(
            img,
            name,
            (x + 5, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

# ---------------------------
# Resize for display
# ---------------------------
img = cv2.resize(img, None, fx=0.2, fy=0.2)

# ---------------------------
# Show result
# ---------------------------
cv2.imshow("RetinaFace - Multiple Faces & Landmarks", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
