import cv2

# Load the image
image = cv2.imread("image1.png")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_gray_image = 255 - gray_image

# Apply Gaussian blur to the inverted grayscale image
blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), sigmaX=0)

# Invert the blurred image to create a pencil sketch
pencil_sketch = 255 - blurred_image

# Display the original image and the pencil sketch
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch", pencil_sketch)

# Save the pencil sketch to a file
cv2.imwrite("pencil_sketch.png", pencil_sketch)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
