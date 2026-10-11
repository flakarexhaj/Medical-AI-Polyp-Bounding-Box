import os
import shutil

# Folderi me të gjitha imazhet
source_folder = "images"

# Folderi ku do të ruhen 100 imazhet
destination_folder = "sample_images"

# Krijo folderin nëse nuk ekziston
os.makedirs(destination_folder, exist_ok=True)

# Merr vetëm file-t e imazheve
image_files = [
    f for f in os.listdir(source_folder)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

# Renditi alfabetikisht
image_files.sort()

# Zgjidh 100 imazhet e para
selected_images = image_files[:100]

# Kopjoji
for image in selected_images:
    source_path = os.path.join(source_folder, image)
    destination_path = os.path.join(destination_folder, image)
    shutil.copy2(source_path, destination_path)

print(f"U kopjuan {len(selected_images)} imazhe.")
print(f"Imazhet ndodhen te: {destination_folder}")

