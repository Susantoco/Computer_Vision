import cv2
import os
import sys
import glob
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from util import save_image

IMAGES_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "images")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "result", "filter", "high_pass")

def laplacian_filter(gray):
    lap = cv2.Laplacian(gray, cv2.CV_64F, ksize=3)
    return cv2.convertScaleAbs(lap)

def sobel_filter(gray):
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobel_x, sobel_y)
    return cv2.convertScaleAbs(sobel_combined)

if __name__ == "__main__":
    image_paths = sorted(glob.glob(os.path.join(IMAGES_DIR, "*.jpg")))

    for image_path in image_paths:
        name = os.path.splitext(os.path.basename(image_path))[0]
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        laplacian = laplacian_filter(gray)
        sobel = sobel_filter(gray)

        save_image(laplacian, f"{name}_laplacian.jpg", OUTPUT_PATH)
        save_image(sobel, f"{name}_sobel.jpg", OUTPUT_PATH)

        print(f"Processed {name}")
