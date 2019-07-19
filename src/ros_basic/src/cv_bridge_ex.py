#!/usr/bin/env python

import rospy
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
from sensor_msgs.msg import Image
import numpy as np
import cv2

rospy.sleep(3)

def cv2_cb(data):
	
	img = cv_bridge.imgmsg_to_cv2(data, "bgr8")
	cv2.imshow("magic",img)
	cv2.waitKey(1)
	rospy.loginfo("in function")



if __name__ == "__main__":
	rospy.init_node("cv2")
	cv_bridge = CvBridge()
	#rospy.loginfo("in function")
	sub = rospy.Subscriber('/usb_cam/image_raw',Image, cv2_cb)
	rospy.spin()

