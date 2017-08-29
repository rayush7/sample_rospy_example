import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np 


def publisher_node():

	cap = cv2.VideoCapture(0)
	image_pub = rospy.Publisher('camera/image',Image,queue_size=10)
	rospy.init_node('publisher_node', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	bridge=CvBridge()

	while not rospy.is_shutdown():

		# Capture frame-by-frame
		ret, frame = cap.read()
		try:
			image_pub.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))
		except CvBridgeError as e:
			print(e)

		rate.sleep()

	cap.release()
	cv2.destroyAllWindows()


if __name__ == '__main__':
	try:
		publisher_node()
	except rospy.ROSInterruptException:
		pass