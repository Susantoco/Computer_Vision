import cv2
import os
import sys
import glob
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from util import save_image

IMAGES_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "images")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "result", "filter", "low_pass")

def mean_filter(img, ksize=5):
    return cv2.blur(img, (ksize, ksize))

def gaussian_filter(img, ksize=5, sigma=0):
    return cv2.GaussianBlur(img, (ksize, ksize), sigma)

if __name__ == "__main__":
    image_paths = sorted(glob.glob(os.path.join(IMAGES_DIR, "*.jpg")))

    for image_path in image_paths:
        name = os.path.splitext(os.path.basename(image_path))[0]
        img = cv2.imread(image_path)

        mean_blur = mean_filter(img, 5)
        gaussian_blur = gaussian_filter(img, 5)

        save_image(mean_blur, f"{name}_mean.jpg", OUTPUT_PATH)
        save_image(gaussian_blur, f"{name}_gaussian.jpg", OUTPUT_PATH)

        print(f"Processed {name}")
