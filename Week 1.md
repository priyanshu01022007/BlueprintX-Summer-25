
## Week 1 Plan: Floor Plan Image Processing Pipeline

## Objective
To learn all the tools required to Build a pipeline to process a floor plan image using OpenCV to detect structural elements like rooms, walls, and contours. The process includes loading, preprocessing, edge detection, line/contour extraction, and exporting results in raster/vector formats.

---

## Resources (Must Go Through)

1. [OpenCV Documentation](https://docs.opencv.org/4.x/index.html) – Core reference for functions and parameters.
2. [YouTube Video – Murtaza's Workshop](https://youtu.be/oXlwWbU8l2o?si=6wjypRnUeV73o_nV) – Watch at least till **2 hours 40 minutes**.
3. [Complete OpenCV Playlist](https://www.youtube.com/playlist?list=PLKnIA16_RmvYXDBJ5WRDuQRSzFJs93pYR) – Watch all videos for a stronger foundation.
4. Feel free to explore additional tutorials, documentation, or blog posts to deepen your understanding.

---

## Minimum Requirements (Compulsory to learn)

### 1.Load and Preprocess the Image

* **Read the image**:
  `cv2.imread()`
* **Convert to grayscale**:
  `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`
* **Denoise using Gaussian Blur**:
  `cv2.GaussianBlur(gray, (5, 5), 0)`
* **Binarize the image**:

  * `cv2.threshold()`
  * or `cv2.adaptiveThreshold()` for uneven lighting
* **(Optional) Remove isolated noise**:
  `cv2.medianBlur()`

---

### 2.Edge Detection

* **Detect edges**:
  `cv2.Canny(gray, minVal, maxVal)`
* Fine-tune `minVal` and `maxVal` to control edge sensitivity.

---

### 3.Line Detection

* **Detect lines**:

  * `cv2.HoughLines()` for infinite-length lines
  * `cv2.HoughLinesP()` for probabilistic finite lines
* **Draw lines**:
  `cv2.line()` to visualize on a blank canvas

---

### 4.Morphological Operations

* **Enhance features**:

  * `cv2.dilate()` to thicken walls
  * `cv2.erode()` to thin out elements
* **Close gaps**:
  `cv2.morphologyEx()` with `cv2.MORPH_CLOSE`

---

### 5.Contour Detection

* **Detect closed contours**:
  `cv2.findContours()`
* **Approximate contours**:
  `cv2.approxPolyDP()`
* **Identify rooms**:

  * `cv2.boundingRect()`
  * or `cv2.minAreaRect()`

---

### 6.Line Refinement (Advanced)

* **Cluster and merge similar lines**:
  Group overlapping or parallel lines
* **Optional Geometry Tools**:
  Use libraries like `Shapely` for robust geometric merging

---

### 7.Export Results

* **Raster Output**:
  `cv2.imwrite()` to save final processed image
* **Vector Output** (SVG/DXF):

  * Use `svgwrite` for SVG
  * Use `ezdxf` for DXF
  * Convert lines and contours manually
