import os
from PIL import Image

# Input & output folder
input_folder = "images"
output_folder = "output"

# Desired size
new_size = (300, 300)  # width x height

# Create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def resize_images():
    for file_name in os.listdir(input_folder):
        try:
            file_path = os.path.join(input_folder, file_name)

            # Skip non-image files
            if not (file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))):
                continue

            # Open image
            img = Image.open(file_path)

            # Resize
            img_resized = img.resize(new_size)

            # Save to output folder (convert all to PNG for example)
            base_name = os.path.splitext(file_name)[0]
            save_path = os.path.join(output_folder, f"{base_name}.png")
            img_resized.save(save_path, "PNG")

            print(f" Resized & saved: {save_path}")

        except Exception as e:
            print(f" Error processing {file_name}: {e}")

if __name__ == "__main__":
    resize_images()
