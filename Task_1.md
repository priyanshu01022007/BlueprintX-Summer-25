**🛠 Task 1: Line Detection and Analysis Pipeline Using OpenCV**

**🎯 Objective:**
Develop a pipeline using OpenCV that can detect straight lines in a given image, redraw those lines on the image, and output the following information for each detected line:

* Starting coordinates `(x1, y1)`
* Ending coordinates `(x2, y2)`
* Slope of the line

**📦 Deliverables:**

1. Python script or Jupyter notebook implementing the pipeline.
2. Output image(s) with detected lines redrawn on them.
3. A structured output (e.g., a CSV or JSON file) listing:

   * Line ID
   * Start point `(x1, y1)`
   * End point `(x2, y2)`
   * Calculated slope
4. Brief documentation or README explaining how to run the pipeline and any dependencies.

**🧭 Guidelines:**

* Use OpenCV functions such as Canny edge detection and Hough Line Transform for line detection.
* Ensure that the redrawn lines are clearly visible (e.g., use a contrasting color and sufficient thickness).
* Handle edge cases such as vertical lines (infinite slope) appropriately.
* If multiple lines are detected close to each other, Handle them carefully.
* Include comments in the code to explain each major step.
* Optional: Allow the script to accept any input image path from the user.
