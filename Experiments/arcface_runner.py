# from deepface import DeepFace
# import numpy as np

# # Returns a list of embeddings, faces, and locations
# result = DeepFace.represent(img_path=r"P:\FaceTech\Face-Tech\Experiments\Aligned_image.png", model_name="ArcFace")

# embedding = result[0]["embedding"]

# em1 = np.array(embedding, dtype=np.float32)

# em1 = em1 / np.linalg.norm(em1)

# cosine_sim = np.dot(em1, em1)
# print(cosine_sim)

import onnxruntime as ort
import numpy as np
from face_preprocessing import normalize_face_input
import cv2

sess = ort.InferenceSession(r"P:\FaceTech\Face-Tech\models\arc.onnx",
                            providers=["CPUExecutionProvider"])

img = cv2.imread("Aligned_image.png")
x = normalize_face_input(img)

input_name = sess.get_inputs()[0].name
emb = sess.run(None, {input_name: x})[0]

# L2 normalize
emb = emb / np.linalg.norm(emb, axis=1, keepdims=True)

print(emb.shape, np.linalg.norm(emb))
