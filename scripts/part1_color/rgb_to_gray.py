import cv2
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from util import save_image

path = os.path.join(os.path.dirname(__file__), "..", "..", "images", "strawberry.jpg")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "result", "color", "rgb_to_gray")

def rgb_to_gray(image_path):
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_gray

if __name__ == "__main__":
    img_gray = rgb_to_gray(path)
    save_image(img_gray, "strawberry_rgb_to_gray.jpg", OUTPUT_PATH)
    cv2.imshow('Grayscale', img_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()