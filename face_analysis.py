import cv2

def analyze_face(face_image):
    # Example feature extraction logic
    height, width = face_image.shape[:2]
    aspect_ratio = width / height
    
    # Show face analysis window
    cv2.imshow('Face Analysis', face_image)
    cv2.waitKey(2000)  # Display for 2 seconds
    cv2.destroyAllWindows()
    
    features = {
        "aspect_ratio": aspect_ratio
    }
    
    return features
