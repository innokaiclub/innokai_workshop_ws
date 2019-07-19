#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('topic_pub')

pub = rospy.Publisher('hello',String)

rate = rospy.Rate(2)

words = "Hello World"

while not rospy.is_shutdown():
	pub.publish(words)
	rate.sleep()
