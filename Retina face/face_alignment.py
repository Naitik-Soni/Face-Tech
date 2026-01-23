import cv2
from retinaface import RetinaFace

images_path = [
    r"../Custom_Data/images/train/04852.png",
]

faces = RetinaFace.extract_faces(img_path = images_path[0], align = True)

for i, face in enumerate(faces):
    b,g,r = cv2.split(face)
    face = cv2.merge([r,g,b])
    
    cv2.imshow(f"face {i}", face)
    
cv2.waitKey(0)
cv2.destroyAllWindows()