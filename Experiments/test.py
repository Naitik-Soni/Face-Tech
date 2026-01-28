import numpy as np
import onnxruntime as ort

print("numpy:", np.__version__)
print("onnxruntime:", ort.__version__)
print("providers:", ort.get_available_providers())