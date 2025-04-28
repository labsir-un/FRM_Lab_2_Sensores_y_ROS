#!/usr/bin/env python3

import rospy
from turtlesim.srv import Spawn, Kill

class TurtleManager:
    def __init__(self):
        
        rospy.wait_for_service('/spawn')
        rospy.wait_for_service('/kill')
        
        self.spawn_srv = rospy.ServiceProxy('/spawn', Spawn)
        self.kill_srv = rospy.ServiceProxy('/kill', Kill)
        
        rospy.loginfo("TurtleManager listo para crear y eliminar tortugas.")

    def spawn_turtle(self, name, x, y, theta):
        """Crea una nueva tortuga"""
        try:
            self.spawn_srv(x=x, y=y, theta=theta, name=name)
            rospy.loginfo(f"Tortuga '{name}' creada en ({x}, {y}, {theta})")
        except rospy.ServiceException as e:
            rospy.logerr(f"Error al crear tortuga: {e}")

    def kill_turtle(self, name):
        """Elimina una tortuga existente"""
        try:
            self.kill_srv(name)
            rospy.loginfo(f"Tortuga '{name}' eliminada.")
        except rospy.ServiceException as e:
            rospy.logerr(f"Error al eliminar tortuga: {e}")

if __name__ == '__main__':
    manager = TurtleManager()
    
    # Ejemplo rápido para probar
    rospy.sleep(1.0)
    manager.spawn_turtle('tortuguita', 5.0, 5.0, 0.0)
    rospy.sleep(2.0)
    manager.kill_turtle('tortuguita')
