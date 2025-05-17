**🛠 Task 2: Propose an Alternative Line Detection Method (Beyond Canny + Hough Transform)**

**🎯 Objective:**
Research and propose an alternative approach to detect straight lines in an image without using the standard OpenCV methods like Canny edge detection or Hough Line Transform. The aim is to understand other viable techniques for line detection and assess their applicability.

**📦 Deliverables:**

1. **Method Description:**

   * Clearly describe the alternative approach.
   * Include a step-by-step breakdown of the pipeline.
   * Explain why this method works for line detection.

2. **Implementation Sketch (Not Full Code):**

   * Pseudocode or flowchart.
   * Outline the tools/libraries used at each step.
   * Mention assumptions and parameters (e.g., thresholding methods, filters).

3. **Resources/References:**

   * Provide links to the papers, tutorials, documentation, or GitHub repositories where the method or its components were found.
   * Briefly summarize how the reference helped shape your approach.

4. **Bonus (Optional):**

   * Add a short comparison with the standard Hough Transform method (advantages/disadvantages).

**🧭 Guidelines:**

* You **must not** use: OpenCV methods
* You **may explore**:

  * **Machine learning-based edge detection** methods like Holistically-Nested Edge Detection (HED)
  * **Gradient-based** methods using Sobel/Scharr filters combined with peak detection or line fitting (e.g., using RANSAC or least squares)
  * **Contour and shape analysis** using OpenCV's `findContours()` and `approxPolyDP()`
  * **Deep Learning approaches** using PyTorch or TensorFlow
  * **scikit-image** features such as `probabilistic_hough_line`, if you analyze its algorithm and don’t directly reuse OpenCV logic

