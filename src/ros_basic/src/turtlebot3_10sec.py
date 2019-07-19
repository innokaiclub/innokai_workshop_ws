#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    #initiate node
    rospy.init_node('robot_cleaner', anonymous=True)
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.sleep(2) #let some time to compute
    rate= rospy.Rate(10)
    #get the time at that exact time
    cmd_vel = Twist()
    time_now = rospy.Time.now()
    rospy.loginfo(time_now)
    while (rospy.Time.now() - time_now  < rospy.Duration(10)):
        cmd_vel.linear.x = 2.0
        cmd_vel.angular.z= 2.0
        cmd_vel_pub.publish(cmd_vel)
        rospy.loginfo(rospy.Time.now() - time_now)

    cmd_vel.linear.x = 0.0

    cmd_vel_pub.publish(cmd_vel)
    rate.sleep()
    rospy.spin()

if __name__ == "__main__":

    move()
