#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.init_node('turtlebot_pub')

turtlesim_twist = Twist()

rate = rospy.Rate(10)
while not rospy.is_shutdown():
	turtlesim_twist.linear.x = 2
	turtlesim_twist.angular.z = 0

	cmd_vel_pub.publish(turtlesim_twist)

	rate.sleep()
