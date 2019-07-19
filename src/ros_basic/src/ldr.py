#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    #front
    rospy.loginfo("Distance for 0 degree is " + str(float("{0:.2f}".format(msg.ranges[0])))+ "m")
    #left
    rospy.loginfo("Distance for 90 degree is " + str(float("{0:.2f}".format(msg.ranges[90]))) + "m")
    #back
    rospy.loginfo("Distance for 180 degree is " + str(float("{0:.2f}".format(msg.ranges[180]))) + "m")
    #right
    rospy.loginfo("Distance for 270 degree is "+ str(float("{0:.2f}".format(msg.ranges[270]))) + "m")



rospy.init_node('topic_sub')
sub = rospy.Subscriber('scan',LaserScan,callback)

rospy.spin()
