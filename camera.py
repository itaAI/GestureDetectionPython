import sys
import cv2

#camera 0 is the integrated webcam on the notebook
camera_port = 0

#no of frames to throw up 
ramp_frames = 30

#initalizing the camera object with function VideoCapture which needs camera port as the parameter
camera = cv2.VideoCapture(camera_port)

#captures a single image from the camera and returns it in PIL format
def getImage():
	#read is the best function to get image
	i=0
	while i<10: 
		retval , im = camera.read()
		return im

for i in xrange(ramp_frames):
	temp = getImage()

print "Getting the image...."
#take the actual image if we want to keep
def videoShow():
	camera_capture = getImage()
	cv2.imshow("abcd" , camera_capture)
	cv2.waitKey(0)

#file = "./images/image.png"
#cv2.imwrite(file, camera_capture)

del(camera)