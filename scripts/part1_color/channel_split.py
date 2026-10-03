import cv2
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from util import save_image

path = os.path.join(os.path.dirname(__file__), "..", "..", "images", "strawberry.jpg")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "result", "color", "channel_split")

def channel_split(image_path):
    img = cv2.imread(image_path)
    b, g, r = cv2.split(img)
    return b, g, r

if __name__ == "__main__":
    b, g, r = channel_split(path)
    save_image(b, "strawberry_blue.jpg", OUTPUT_PATH)
    save_image(g, "strawberry_green.jpg", OUTPUT_PATH)
    save_image(r, "strawberry_red.jpg", OUTPUT_PATH)
    cv2.imshow('Blue Channel', b)
    cv2.imshow('Green Channel', g)
    cv2.imshow('Red Channel', r)
    print("B channel:")
    print(b)

    print("G channel:")
    print(g)

    print("R channel:")
    print(r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()