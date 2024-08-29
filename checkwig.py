import os

def check_wig_data():
    wig_data_path = r"C:\Users\vrinda\Downloads\WigData\images.cv_0dsve44hwuhggjmvm8ch4ug\data"
    for folder in ["train", "val", "test"]:
        folder_path = os.path.join(wig_data_path, folder)
        if os.path.exists(folder_path):
            print(f"Checking folder: {folder_path}")
            files = os.listdir(folder_path)
            print(f"Contents of {folder_path}: {files}")
            if not files:
                print(f"Folder {folder_path} is empty.")
            else:
                for file in files:
                    if file.endswith(".jpg") or file.endswith(".png"):
                        print(f"Found image file: {file}")
        else:
            print(f"Folder does not exist: {folder_path}")

check_wig_data()
