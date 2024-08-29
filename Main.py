from face_detection import detect_face
from face_analysis import analyze_face
from wig import recommend_wig, show_wig_recommendation

def main():
    face_detected, face_image = detect_face()
    if not face_detected:
        print("No face detected. Exiting.")
        return
    
    features = analyze_face(face_image)
    wig_recommendation = recommend_wig(features)
    
    if wig_recommendation:
        show_wig_recommendation(wig_recommendation)
    else:
        print("No wig recommendation available.")

if __name__ == "__main__":
    main()
