#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):

    if  msg.ranges[0] < 1:
        cmd_vel.linear.x = 0
    else:
        cmd_vel.linear.x = 0.1
    cmd_vel_pub.publish(cmd_vel)
    rate.sleep()

rospy.init_node('topic_sub')
cmd_vel = Twist()
rate = rospy.Rate(10)
cmd_vel_pub=rospy.Publisher('cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('scan',LaserScan,callback)

rospy.spin()
