#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose 

def poseMessageReceived(message):
    rospy.loginfo(f'position=({message.x}, {message.y}) direction= {message.theta}')

if __name__ == '__main__':
    try:
        rospy.init_node('pysubpose', anonymous=False)
        sub = rospy.Subscriber('turtle1/pose', Pose, poseMessageReceived) 

        rospy.spin()

    except rospy.ROSInterruptException:
        pass