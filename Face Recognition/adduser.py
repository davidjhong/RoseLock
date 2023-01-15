# program to capture single image from webcam in python

# importing OpenCV library
import cv2
import os

# initialize the camera
# If you have multiple camera connected with
# current device, assign a value in cam_port
# variable according to that
cam = cv2.VideoCapture(0)

# reading the input using the camera
result, image = cam.read()
path = "faces" #Set where you want the images to be saved in

# If image will detected without any error,
# show result
if result:

	# showing result, it take frame name and image
	# output
	cv2.imshow("captured image", image)

	# saving image in local storage
	cv2.imwrite(os.path.join(path, "cap1.png"), image)

	# If keyboard interrupt occurs, destroy image
	# window
	cv2.waitKey(0)
	cv2.destroyWindow("Did not work try again")

# If captured image is corrupted, moving to else part
else:
	print("No image detected. Please! try again")
