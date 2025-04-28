#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty
import sys
import termios
import tty

class BackgroundChanger:
    def __init__(self):
        
        # Espera el servicio para limpiar la pantalla
        rospy.wait_for_service('/clear')  
        self.clear_srv = rospy.ServiceProxy('/clear', Empty)

        # Diccionario de colores para el fondo
        self.colors = {
            'r': (255, 100, 100),
            'g': (100, 255, 100),
            'b': (100, 100, 255),
            'w': (225, 225, 225),
            'k': (100, 100, 100)
        }

        rospy.loginfo("Presiona r/g/b/w/k para cambiar el color del fondo de turtlesim")

    def get_key(self):
        """Lee una tecla del teclado (modo no bloqueante)"""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key

    def change_background(self, r, g, b):
        """Cambia el color de fondo en turtlesim"""
        rospy.set_param('/turtlesim/background_r', r)
        rospy.set_param('/turtlesim/background_g', g)
        rospy.set_param('/turtlesim/background_b', b)
        self.clear_srv()  # Llama el servicio para limpiar y aplicar el cambio
        rospy.loginfo(f"Color de fondo cambiado a: R={r}, G={g}, B={b}")

    def run(self):
        """Corre el bucle que escucha las teclas y cambia el color de fondo"""
        while not rospy.is_shutdown():
            key = self.get_key()
            if key in self.colors:
                r, g, b = self.colors[key]
                self.change_background(r, g, b)
            elif key == '\x03':  # Ctrl-C
                break

if __name__ == '__main__':
    try:
        changer = BackgroundChanger()
        changer.run()
    except rospy.ROSInterruptException:
        pass
