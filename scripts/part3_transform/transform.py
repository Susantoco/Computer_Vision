import cv2
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from util import save_image

path = os.path.join(os.path.dirname(__file__), "..", "..", "images", "strawberry.jpg")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "result", "transform")


def translate(img, tx, ty):
    h, w = img.shape[:2]
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    return cv2.warpAffine(img, M, (w, h))


def rotate(img, angle, scale=1.0):
    h, w = img.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(img, M, (w, h))


def scale_image(img, fx, fy):
    return cv2.resize(img, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)


def affine_transform(img, src_pts, dst_pts):
    h, w = img.shape[:2]
    M = cv2.getAffineTransform(np.float32(src_pts), np.float32(dst_pts))
    return cv2.warpAffine(img, M, (w, h))


def projective_transform(img, src_pts, dst_pts):
    h, w = img.shape[:2]
    M = cv2.getPerspectiveTransform(np.float32(src_pts), np.float32(dst_pts))
    return cv2.warpPerspective(img, M, (w, h))


if __name__ == "__main__":
    img = cv2.imread(path)
    h, w = img.shape[:2]

    translated = translate(img, tx=60, ty=40)
    rotated = rotate(img, angle=30)
    scaled = scale_image(img, fx=0.6, fy=0.6)

    affine_src = [[0, 0], [w - 1, 0], [0, h - 1]]
    affine_dst = [[0, h * 0.1], [w * 0.9, 0], [w * 0.1, h * 0.9]]
    affine = affine_transform(img, affine_src, affine_dst)

    proj_src = [[0, 0], [w - 1, 0], [0, h - 1], [w - 1, h - 1]]
    proj_dst = [[w * 0.1, h * 0.2], [w * 0.9, 0], [0, h - 1], [w - 1, h * 0.8]]
    projective = projective_transform(img, proj_src, proj_dst)

    save_image(translated, "strawberry_translated.jpg", OUTPUT_PATH)
    save_image(rotated, "strawberry_rotated.jpg", OUTPUT_PATH)
    save_image(scaled, "strawberry_scaled.jpg", OUTPUT_PATH)
    save_image(affine, "strawberry_affine.jpg", OUTPUT_PATH)
    save_image(projective, "strawberry_projective.jpg", OUTPUT_PATH)

    print("Done. Results saved to", OUTPUT_PATH)
