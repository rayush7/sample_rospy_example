import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np 

class subscriber_node:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("camera/image",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    cv_image=cv2.cvtColor(cv_image,cv2.COLOR_BGR2YUV)

    cv2.imshow("Subscriber Window", cv_image)
    cv2.waitKey(3)

#-------------------------------------------------------------------------------

def main():
	ic = subscriber_node()
	rospy.init_node('subscriber_node', anonymous=True)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()