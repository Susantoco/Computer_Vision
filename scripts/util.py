import cv2
import os

def save_image(image, filename, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    cv2.imwrite(os.path.join(output_path, filename), image)