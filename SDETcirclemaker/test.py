import cv2
import numpy as np
image = cv2.imread(r'C:\Users\Kaveen\PycharmProjects\holoplot\SDETcirclemaker\test.png')
image1 = cv2.imread(r'C:\Users\Kaveen\PycharmProjects\holoplot\SDETcirclemaker\test1.png')
image2 = cv2.imread(r'C:\Users\Kaveen\PycharmProjects\holoplot\SDETcirclemaker\test2.png')
image3 = cv2.imread(r'C:\Users\Kaveen\PycharmProjects\holoplot\SDETcirclemaker\test3.png')

output = image.copy()
li = [image,image1,image2,image3]
for i in li:
	gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
	cv2.imshow("Gray image", gray)
	# cv2.waitKey(0)
	#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,1,100,
							param1=50,param2=24,minRadius=15,maxRadius=0)
	print(circles)
	# # ensure at least some circles were found
	# if circles is not None:
	# 	# convert the (x, y) coordinates and radius of the circles to integers
	# 	circles = np.round(circles[0, :]).astype("int")
	# 	# loop over the (x, y) coordinates and radius of the circles
	# 	for (x, y, r) in circles:
	# 		# draw the circle in the output image, then draw a rectangle
	# 		# corresponding to the center of the circle
	# 		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
	# 		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	# 	# show the output image
	# 	cv2.imshow("output", np.hstack([image, output]))
	# 	# cv2.waitKey(0)