import cv2 as cv

# Load the image
img = cv.imread("Nishinoya.jpg")

if img is None:
  print("Cannot open image")
else:
  # Resize the image
  img = cv.resize(img, (300, 300))

  # Convert the image to grayscale
  # `cv.cvtColor` convert an image from one color space to another
  # Usage: cv.cvtColor(<input image>, <color conversion code>)
  img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

  # Display the image
  cv.imshow("Image", img)

  # Wait for the user to press any key
  cv.waitKey(0)

  cv.destroyAllWindows()

# TODO: Edge detection