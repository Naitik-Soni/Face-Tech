import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from retinaface import RetinaFace

resp = RetinaFace.detect_faces(r"..\Custom_Data\images\train\04875.png")

print(resp)
print(type(resp))