## Setup
Install dependencies:
```
pip install -r requirements.txt
```

## Run source
### Part 1: Color
Convert RGB to grayscale:
```
python scripts/part1_color/rgb_to_gray.py
```
Convert grayscale back to RGB:
```
python scripts/part1_color/gray_to_rgb.py
```
Split channel:
```
python scripts/part1_color/channel_split.py
```
Combine channel:
```
python scripts/part1_color/channel_combination.py
```
### Part 2: Filter
Runs on every image in `images/`.

Low-pass (mean + Gaussian):
```
python scripts/part2_filter/low_pass.py
```
High-pass (Laplacian + Sobel):
```
python scripts/part2_filter/high_pass.py
```
### Part 3: Transform
Translation, rotation, scaling, affine, projective (saves results to `result/transform/`):
```
python scripts/part3_transform/transform.py
```
Visual comparison notebook (affine vs projective):
```
scripts/part3_transform/part3_transform.ipynb
```
