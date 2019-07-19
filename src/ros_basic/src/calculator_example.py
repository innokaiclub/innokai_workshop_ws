#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('calculator')

pub = rospy.Publisher('result',Int32)

rate = rospy.Rate(2)

group1 = [99, 88 ,77]
group2 = [77, 88, 99]

while not rospy.is_shutdown():
	for n in range(3):
		difference = group1[n] - group2[n]
		pub.publish(difference)
	rate.sleep()
