#!/usr/bin/env python3

import rospy
from turtlesim.srv import TeleportAbsolute
from std_srvs.srv import Empty


if __name__=='__main__':

    try:

        rospy.init_node('turtlesimservice',anonymous=False)
        rospy.wait_for_service('turtle1/teleport_absolute')

        turtle1_teleport=rospy.ServiceProxy('turtle1/teleport_absolute',TeleportAbsolute)

        rospy.wait_for_service('clear')
        clear1=rospy.ServiceProxy('clear',Empty)

        rate=rospy.Rate(0.3)

        pos=1
        #Similartowhile(ros::ok())
        while not rospy.is_shutdown():
            
            if(pos==1):
                resp1=turtle1_teleport(4, 5, 0)
                clear1()
            if(pos==2):
                resp1=turtle1_teleport(4, 10, 0)
            if(pos==3):
                resp1=turtle1_teleport(8, 10, 0)
            if(pos==4):
                resp1=turtle1_teleport(8, 5, 0)
            if(pos==5):
                resp1=turtle1_teleport(4, 5, 0)
            if(pos>5):
                pos=1
            
            pos+=1
            rate.sleep()

    except rospy.ROSInterruptException:
        pass