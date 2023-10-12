import os
from pdf2image import convert_from_path
import shutil

# Directories
pdf_dir = 'pdf'
png_dir = 'png'
archive_dir = 'pdf_archive'

# Create the png and pdf_archive directories if they don't exist
if not os.path.exists(png_dir):
    os.makedirs(png_dir)

if not os.path.exists(archive_dir):
    os.makedirs(archive_dir)

# Loop through all files in the pdf directory
for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_dir, filename)
        
        # Convert the PDF to images
        images = convert_from_path(pdf_path)
        
        # Save each page of the PDF as an image in the png directory
        for i, image in enumerate(images):
            image_path = os.path.join(png_dir, f"{filename[:-4]}_page_{i + 1}.png")
            image.save(image_path, 'PNG')
        
        # Move the processed PDF to the archive directory
        shutil.move(pdf_path, os.path.join(archive_dir, filename))

print("Conversion and archiving complete!")
