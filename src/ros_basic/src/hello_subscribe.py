#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(msg):
	rospy.loginfo(msg.data)

rospy.init_node('topic_sub')
sub = rospy.Subscriber('hello',String,callback)

rospy.spin()
