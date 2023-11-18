import fitz
from PIL import Image
import os
import numpy as np
import shutil

pdf_path = "2023-EROLLGEN-S29-50-FinalRoll-Revision1-TEL-9_231118_222327.pdf"

doc = fitz.open(pdf_path)
if os.path.exists('images'):
    shutil.rmtree('images')
if os.path.exists('data'):
        shutil.rmtree('data')    
os.makedirs('images', exist_ok=True)
count = 1
for i in range(2, len(doc) - 1):
    pixmap = doc[i].get_pixmap()

    image_file = f"images/output_image{i}.png"
    pixmap.save(image_file)

    image = Image.open(image_file)

    os.makedirs('data', exist_ok=True)
    for y in range(10):
        for x in range(3):
            i = x * 190
            j = y * 80
            coordinates = [(155+i, 45+j), (195+i, 90+j)]
            cropped_image = image.crop((*coordinates[0], *coordinates[1]))

            image_data = np.array(cropped_image)
            if not np.all(image_data == [255, 255, 255]): 
                cropped_image.save(os.path.join('data', str(count) + '.jpg'))
                count += 1