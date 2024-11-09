import os
from PIL import Image

def rotate_images_in_folder(input_folder_path, rotation_angle=90):
    # Check if the folder path exists
    if not os.path.isdir(input_folder_path):
        print(f"The folder '{input_folder_path}' does not exist.")
        return
    
    # Create an output folder for the rotated images
    output_folder = os.path.join(input_folder_path, "rotated_images")
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through each file in the folder
    for filename in os.listdir(input_folder_path):
        file_path = os.path.join(input_folder_path, filename)
        
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                # Open the image
                with Image.open(file_path) as img:
                    # Rotate the image
                    rotated_img = img.rotate(rotation_angle, expand=True)
                    # Save the rotated image in the output folder
                    rotated_img.save(os.path.join(output_folder, filename))
                    print(f"Rotated and saved: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Usage
FOLDER_PATH = "{Add path}"  # Replace with your folder path
rotate_images_in_folder(FOLDER_PATH)
