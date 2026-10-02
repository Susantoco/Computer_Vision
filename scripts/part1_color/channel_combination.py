import cv2
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from util import save_image

path = os.path.join(os.path.dirname(__file__), "..", "..", "images", "strawberry.jpg")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "result", "color", "channel_combination")

def reconstruct_image(b, g, r):
    return cv2.merge([b, g, r])

def swap_channels(b, g, r):
    return cv2.merge([r, g, b])

def zero_out_channel(b, g, r, channel):
    zeros = b * 0
    if channel == "b":
        return cv2.merge([zeros, g, r])
    if channel == "g":
        return cv2.merge([b, zeros, r])
    if channel == "r":
        return cv2.merge([b, g, zeros])
    raise ValueError("channel must be 'b', 'g' or 'r'")

if __name__ == "__main__":
    img = cv2.imread(path)
    b, g, r = cv2.split(img)

    reconstructed = reconstruct_image(b, g, r)
    swapped = swap_channels(b, g, r)
    no_red = zero_out_channel(b, g, r, "r")
    no_green = zero_out_channel(b, g, r, "g")
    no_blue = zero_out_channel(b, g, r, "b")

    save_image(reconstructed, "strawberry_reconstructed.jpg", OUTPUT_PATH)
    save_image(swapped, "strawberry_swapped_rb.jpg", OUTPUT_PATH)
    save_image(no_red, "strawberry_no_red.jpg", OUTPUT_PATH)
    save_image(no_green, "strawberry_no_green.jpg", OUTPUT_PATH)
    save_image(no_blue, "strawberry_no_blue.jpg", OUTPUT_PATH)

    cv2.imshow('Original', img)
    cv2.imshow('Reconstructed', reconstructed)
    cv2.imshow('Swapped R-B', swapped)
    cv2.imshow('No Red', no_red)
    cv2.imshow('No Green', no_green)
    cv2.imshow('No Blue', no_blue)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
