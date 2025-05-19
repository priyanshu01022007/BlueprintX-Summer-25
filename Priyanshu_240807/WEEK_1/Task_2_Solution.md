# WEEK 1; TASK 2 SOLUTION

## **Gradient-Based Line Detection + RANSAC Line Fitting**

- Detect edges using Canny and then apply Hough Transform  
- Detect edges using gradient filters (Sobel)  
- Use RANSAC to fit straight lines on these points

---

## **Pipeline Breakdown (Step By Step)**

### 1. **Grayscale Conversion**
- Convert the image to grayscale to simplify processing.

### 2. **Apply Gradient Filter (Sobel)**
- \( G_x \) = Sobel horizontal gradient (x-axis)  
- \( G_y \) = Sobel vertical gradient (y-axis)  
- \( G \) = Gradient magnitude  
  \[
  G = \sqrt{G_x^2 + G_y^2}
  \]

### 3. **Thresholding the Gradient Magnitude**
- Finding strong edges  
- Threshold = 100  
  \[
  \text{Edges} = G > 100
  \]

### 4. **Get Coordinates of Non-Zero Pixels in Edges**
- Extract coordinates \((x, y)\) of all non-zero pixels in the thresholded gradient image.

### 5. **Line Fitting using RANSAC**
- Input: Set of edge points  
- Use RANSAC regression to:
  - Fit a line using the above points
  - Identify inliers (points that are close to the line)
- Remove inliers and repeat until no significant sets remain.

### 6. **Result**
- Get starting point \((x_1, y_1)\):  
  \[
  x_1 = \min(\text{inlier}_x),\quad y_1 = \min(\text{inlier}_y)
  \]

- Get ending point \((x_2, y_2)\):  
  \[
  x_2 = \max(\text{inlier}_x),\quad y_2 = \max(\text{inlier}_y)
  \]

- Slope:  
  \[
  \text{slope} = 
    \begin{cases}
      \text{"undefined"} & \text{if } x_1 = x_2 \\
      \frac{y_2 - y_1}{x_2 - x_1} & \text{otherwise}
    \end{cases}
  \]

---

## **Pseudocode**

```python
# Step 1: Read and preprocess
img = read_image('PATH_OF_IMAGE')
gray = cvtColor(img, COLOR_BGR2GRAY)

# Step 2: Apply Gradient filter
Gx = sobel(gray, axis='x')
Gy = sobel(gray, axis='y')
G = sqrt((Gx**2) + (Gy**2))

# Step 3: Threshold to get edges
edges = G > Threshold
edge_points = get_nonzero_coordinates(edges)

# Step 4: Fit lines using RANSAC
while len(edge_points) > 0:
    line_model = run_RANSAC(edge_points)
    inliers = get_points_close_to_line(line_model, edge_points)

    if len(inliers) < MIN_INLIERS:
        break

    lines.append(line_model)
    edge_points = edge_points - inliers

# Step 5: Output
for line in lines:
    x1, y1, x2, y2 = get_line_endpoints(line)
    if x1 == x2:
        slope = 'undefined'
    else:
        slope = (y2 - y1) / (x2 - x1)
    draw.line(pt1=(x1, y1), pt2=(x2, y2), color=(255, 255, 255), thickness=1)
    imshow(Line)

***Resources/References***
1. **RANSAC Regression**
    It helped implement robust line fitting that can reject outliers.
    link - https://www.youtube.com/watch?v=BHNNz6jCuHw
2. **Sobel Edge Detection**
    Used to compute horizontal and vertical gradients
    link - https://www.youtube.com/watch?v=Yz7h9L4gecQ
3. **Canny and Hough Transform**
    To detecting edges and print lines
    link (Canny Edge Detection) - https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html#autotoc_md1302
    link (Hough Line Transform) - https://docs.opencv.org/4.x/d6/d10/tutorial_py_houghlines.html
