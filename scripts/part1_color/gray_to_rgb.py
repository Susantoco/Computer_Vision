import cv2
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from util import save_image

path = os.path.join(os.path.dirname(__file__), "..", "..", "images", "strawberry.jpg")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "result", "color", "gray_to_rgb")

def gray_to_rgb(image_path):
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_back = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    return img_gray, img_back

if __name__ == "__main__":
    img_gray, img_back = gray_to_rgb(path)
    save_image(img_back, "strawberry_gray_to_rgb.jpg", OUTPUT_PATH)
    cv2.imshow('Grayscale', img_gray)
    cv2.imshow('Gray converted back to RGB', img_back)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
