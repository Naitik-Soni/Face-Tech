import numpy as np
import cv2

def rotate_face(image_path, landmarks):
    image = cv2.imread(image_path)

    left_eye = landmarks.get("landmarks").get("left_eye")
    right_eye = landmarks.get("landmarks").get("right_eye")

    dx = right_eye[0] - left_eye[0]
    dy = right_eye[1] - left_eye[1]

    angle = np.degrees(np.arctan2(dy, dx)) - 180

    eyes_center = [
        int((left_eye[0] + right_eye[0])/2),
        int((left_eye[1] + right_eye[1])/2)
    ]

    M = cv2.getRotationMatrix2D(
        center=eyes_center,
        angle=angle,
        scale=1.0
    )

    aligned_image = cv2.warpAffine(
        image,
        M,
        (image.shape[1], image.shape[0]),
        flags=cv2.INTER_CUBIC
    )

    right_eye = rotate_point(M, (right_eye[0], right_eye[1]))
    left_eye = rotate_point(M, (left_eye[0], left_eye[1]))


def rotate_point(M, point):
    x, y = point
    new_x = M[0,0]*x + M[0,1]*y + M[0,2]
    new_y = M[1,0]*x + M[1,1]*y + M[1,2]
    return (int(new_x), int(new_y))