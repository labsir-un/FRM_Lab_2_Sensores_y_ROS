#!/usr/bin/env python3
import rospy
import sys
import termios
import tty

# Importar los módulos de la misma estructura de paquete
from laboratorio_2.background_changer import BackgroundChanger
from laboratorio_2.turtle_manager import TurtleManager

class Controller:
    def __init__(self):
        rospy.init_node('turtle_controller', anonymous=True)
        
        # Inicializar el cambiador de fondo y el administrador de tortugas
        self.bg_changer = BackgroundChanger()
        self.manager = TurtleManager()
        
        self.colors = self.bg_changer.colors  # Reutilizamos los colores definidos en BackgroundChanger
        
        rospy.loginfo("Controlador activo:")
        rospy.loginfo("- r/g/b/w/k para cambiar color de fondo")
        rospy.loginfo("- c para crear una tortuga")
        rospy.loginfo("- d para eliminar una tortuga")
        rospy.loginfo("- Ctrl-C para salir")
    
    def get_key(self):
        """Lee una tecla del teclado (modo no bloqueante)."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key

    def run(self):
        """Controla el flujo de entrada del teclado para las diferentes acciones"""
        while not rospy.is_shutdown():
            key = self.get_key()
            
            if key in self.colors:
                # Cambia el color de fondo según la tecla presionada
                r, g, b = self.colors[key]
                self.bg_changer.change_background(r, g, b)
            
            elif key == 'c':
                # Crear una nueva tortuga
                name = input("\nNombre de la nueva tortuga: ")
                x = float(input("X posición (0-11): "))
                y = float(input("Y posición (0-11): "))
                theta = float(input("Ángulo (radianes): "))
                self.manager.spawn_turtle(name, x, y, theta)
            
            elif key == 'd':
                # Eliminar una tortuga
                name = input("\nNombre de la tortuga a eliminar: ")
                self.manager.kill_turtle(name)

            elif key == '\x03':  # Ctrl-C
                break

if __name__ == '__main__':
    try:
        controller = Controller()
        controller.run()
    except rospy.ROSInterruptException:
        pass
