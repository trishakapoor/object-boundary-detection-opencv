import cv2
import os


# -----------------------------
# Paths
# -----------------------------
INPUT_PATH = "input/input.jpg"
OUTPUT_DIR = "output"


# -----------------------------
# Create output directory
# -----------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)


# -----------------------------
# Read input image
# -----------------------------
image = cv2.imread(INPUT_PATH)

if image is None:
    print(f"Error: Could not read image from '{INPUT_PATH}'")
    print("Make sure the image exists and is named 'input.jpg'.")
    exit(1)

print("Input image loaded successfully.")


# -----------------------------
# 1. Grayscale Conversion
# -----------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite(
    os.path.join(OUTPUT_DIR, "grayscale.jpg"),
    gray
)


# -----------------------------
# 2. Gaussian Smoothing
# -----------------------------
blurred = cv2.GaussianBlur(
    gray,
    (5, 5),
    0
)

cv2.imwrite(
    os.path.join(OUTPUT_DIR, "blurred.jpg"),
    blurred
)


# -----------------------------
# 3. Canny Edge Detection
# -----------------------------
edges = cv2.Canny(
    blurred,
    50,
    150
)

cv2.imwrite(
    os.path.join(OUTPUT_DIR, "edges.jpg"),
    edges
)


# -----------------------------
# 4. Morphological Closing
# -----------------------------
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (5, 5)
)

morphology = cv2.morphologyEx(
    edges,
    cv2.MORPH_CLOSE,
    kernel
)

cv2.imwrite(
    os.path.join(OUTPUT_DIR, "morphology.jpg"),
    morphology
)


# -----------------------------
# 5. Contour Extraction
# -----------------------------
contours, hierarchy = cv2.findContours(
    morphology,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)


# -----------------------------
# 6. Draw Boundaries
# -----------------------------
final_image = image.copy()

cv2.drawContours(
    final_image,
    contours,
    -1,
    (0, 255, 0),
    2
)

cv2.imwrite(
    os.path.join(OUTPUT_DIR, "final_boundaries.jpg"),
    final_image
)


# -----------------------------
# 7. Display results
# -----------------------------
print("---------------------------------------")
print("Object Boundary Detection Completed")
print("---------------------------------------")
print(f"Number of detected contours: {len(contours)}")
print(f"Results saved in: {OUTPUT_DIR}/")
print()
print("Generated files:")
print("1. grayscale.jpg")
print("2. blurred.jpg")
print("3. edges.jpg")
print("4. morphology.jpg")
print("5. final_boundaries.jpg")
