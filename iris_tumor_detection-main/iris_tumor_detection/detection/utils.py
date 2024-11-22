import cv2
import numpy as np
import joblib
from django.core.files.uploadedfile import InMemoryUploadedFile

# Load the trained model
model_path = 'detection/svm_model.pkl'  # Update this path as necessary
svm_model = joblib.load(model_path)

def preprocess_image(image: InMemoryUploadedFile):
    # Convert to OpenCV format
    file_bytes = np.frombuffer(image.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Check if the image is valid
    if img is None:
        raise ValueError("Invalid image provided")
    
    # Resize to match the original model input
    img_resized = cv2.resize(img, (64, 64))
    
    # Flatten the array to match the input shape expected by the SVM model
    img_flattened = img_resized.flatten().reshape(1, -1)  # Should be (1, 12288)
    
    return img_flattened

def detect_tumor(image: InMemoryUploadedFile):
    features = preprocess_image(image)
    
    # Predict using the SVM model
    prediction = svm_model.predict(features)
    
    return prediction[0]  # Return the prediction (0 or 1)

# Example usage in Django view
def handle_uploaded_image(image: InMemoryUploadedFile):
    result = detect_tumor(image)
    if result == 1:
        return "Tumor detected"
    else:
        return "No tumor detected"
    
    

