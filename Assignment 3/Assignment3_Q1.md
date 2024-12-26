### Method 1

Grayscale Conversion: Simplifies image processing by reducing the image to a single intensity channel instead of three (RGB).
Thresholding: Converts the grayscale image into a binary image for easier processing.
Edge Detection: Identifies changes in intensity (edges) by calculating differences between neighboring pixels.
Summing Edge Intensities: Aggregates edge information across rows and columns to detect potential regions with highest number of edges(flag).
Bounding Box Detection: Determines the rectangular region containing the flag based on edge intensity.
Cropping and Resizing: Standardizes the flag region for easier classification. Splits the flag into top and bottom halves and computes mean intensity to classify the flag.
Classifies the flag as "Indonesia" or "Poland".(If top half is darker than bottom half, result is Indonesia)

### Method 2

Code started with reading the image and converting it to BGR.
Color Segmentation: Specific ranges for red and white colors are defined in HSV format.
Edge Detection: Canny Edge Detection is applied to detect edges in the masks. This helps identify the contours and boundaries of regions matching the color criteria.
Contour Detection: Contours in the binary edge-detected image are extracted using cv2.findContours. These contours represent the boundaries of detected shapes, which may correspond to flag regions.
The vertical positions of red and white pixel regions are extracted and compared. The average y-coordinates (np.mean) help determine if white is above red or not.
Classification: Based on the relative positions of the red and white regions, the code determines whether the flag is "Poland" or "Indonesia".