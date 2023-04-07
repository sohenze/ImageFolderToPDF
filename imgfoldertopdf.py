import img2pdf
import os
import sys

from pathlib import Path

# Arg checking
if len(sys.argv) > 2:
    raise Exception("Input only 1 target directory")

# Include list of extensions to convert here
include_ext = [".jpg" , ".jpeg" , ".jpe" , ".jif" , ".jfif", ".png"]

# Img Buffer
imgs = []

# Max number of images/pages per pdf, insert into new pdf if exceeded
threshold = 1000

# Counters for pdfs and imgs
pdf_count = 1
img_count = 0

target_dir = sys.argv[1]
root_path = str(Path(target_dir).parent.absolute()) + '\\'

# Iterate through files only
for root, dirs, files in os.walk(target_dir):
    for file in files:
        file_path = os.path.join(root, file)
        
        # Skip files not in include_ext list
        body, ext = os.path.splitext(file_path)
        if ext not in include_ext:
            continue

        # Add img to buffer
        imgs.append(file_path)
        img_count += 1

        # Add img to pdf once max page number reached
        if img_count >= threshold:
            file_name = Path(target_dir).name + str(pdf_count) + '.pdf'
            output_path = root_path + file_name

            with open(output_path, "wb") as f:
                pfd_data = img2pdf.convert(imgs)
                f.write(pfd_data)

            # Reset buffer and update counters for new pdf
            imgs = []
            img_count = 0
            pdf_count += 1

# Add remaining imgs left in buffer
if len(imgs) > 0:
    file_name = Path(target_dir).name + str(pdf_count) + '.pdf'
    output_path = root_path + file_name

    with open(output_path, "wb") as f:
        pfd_data = img2pdf.convert(imgs)
        f.write(pfd_data)
            