# object-boundary-detection-opencv

# Object Boundary Detection Using Image Processing

A simple computer vision project that detects and highlights object boundaries in an image using Python and OpenCV.

## Technologies

* Python 3
* OpenCV
* NumPy
* Visual Studio Code

## Processing Pipeline

```text
Input Image
    ↓
Grayscale Conversion
    ↓
Gaussian Blur
    ↓
Canny Edge Detection
    ↓
Morphological Closing
    ↓
External Contour Extraction
    ↓
Boundary Drawing
    ↓
Output Images
```

## Project Structure

```text
Computer_Vision_Object_Boundary_Detection/
├── input/
│   └── input.jpg
├── output/
├── src/
│   └── main.py
├── requirements.txt
└── README.md
```

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Input

Place the image to be processed at:

```text
input/input.jpg
```

## Run

From the project root directory:

```bash
python src/main.py
```

## Output

The program generates the following files inside the `output` directory:

* `grayscale.jpg`
* `blurred.jpg`
* `edges.jpg`
* `morphology.jpg`
* `final_boundaries.jpg`

The final image contains the detected external contours drawn in green on the original image.

## Parameters

### Gaussian Blur

```python
(5, 5)
```

A 5 × 5 Gaussian kernel is used for smoothing.

### Canny

```python
50, 150
```

The lower and upper Canny thresholds are 50 and 150.

### Morphological Closing

A 5 × 5 rectangular structuring element is used.

## Limitations

* Background textures can produce unwanted edges.
* Fixed Canny thresholds may not work equally well for all images.
* Low contrast can reduce boundary quality.
* Touching objects can produce connected contours.
* The system does not identify object classes.
* The current implementation processes one still image at a time.
