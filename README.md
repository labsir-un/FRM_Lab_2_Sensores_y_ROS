<div align="center">
<picture>
    <source srcset="https://imgur.com/5bYAzsb.png" media="(prefers-color-scheme: dark)">
    <source srcset="https://imgur.com/Os03JoE.png" media="(prefers-color-scheme: light)">
    <img src="https://imgur.com/Os03JoE.png" alt="Escudo UNAL" width="350px">
</picture>

<h3>Curso de Fundamentos de Robótica Móvil</h3>

<h1>Introducción al uso de sensores</h1>

<h2>Guía 2 - Introducción al uso de sensores y ROS</h2>

<h5>Pedro F. Cárdenas<br>
    Ricardo Ramírez<br>
    Juan S. Daleman</h5>

<h6>Universidad Nacional de Colombia<br>
    Facultad de Ingeniería<br>
    Departamento de Ingeniería Mecánica y Mecatrónica<br>
    Bogotá, Colombia<br>
    2025</h6>
</div>

<details>
    <summary>🗂️ Tabla de Contenido</summary>

<!-- TOC -->
- [1. 📖 Introducción](#1--introducción)
- [2. 🎯 Objetivos](#2--objetivos)
- [3. 🧰 Herramientas Necesarias](#3--herramientas-necesarias)
  - [3.1. 🔭🛠️ Equipos](#31-️-equipos)
  - [3.2. 🖥️💾 Software](#32-️-software)
- [4. 🔧➡️🚀 Procedimiento](#4-️-procedimiento)
  - [4.1. 🔍📚 Búsqueda bibliográfica](#41--búsqueda-bibliográfica)
  - [4.2. Sensor HOKUYO](#42-sensor-hokuyo)
  - [4.3. Sensor RPLIDAR](#43-sensor-rplidar)
  - [4.4. Sensor de ultrasonido](#44-sensor-de-ultrasonido)
  - [4.5. Sensores Lego](#45-sensores-lego)
  - [4.6. ROS](#46-ros)
  - [4.7. ROS Kuboki](#47-ros-kuboki)
  - [4.8. ROS Lego EV3](#48-ros-lego-ev3)
- [5. 📚🔗 Recursos](#5--recursos)


</details>

---

<h1> 👁️🧠🤖 Guía 2: Introducción al uso de sensores y ROS </h1>

## 1. 📖 Introducción

Los sensores son elementos fundamentales para que los robots móviles puedan cumplir con su función. Estos dispositivos poseen un conjunto de características técnicas que se clasifican en características estáticas y características dinámicas. Asociadas a dichas características existe un conjunto de valores de error que conforman la incertidumbre de medida.

A medida que se busca un mejor desempeño de los robots, estos errores se vuelven más evidentes y adquieren mayor relevancia. Reconocer su existencia, magnitud y comportamiento permite controlarlos mediante el preprocesamiento de señales, o al menos identificar por qué el comportamiento del robot difiere del esperado.

En este contexto, el uso de ROS (Robot Operating System) se ha convertido en un estándar fundamental para el desarrollo de robots móviles. ROS proporciona una infraestructura flexible que facilita la integración de diversos componentes de hardware, como sensores, actuadores y unidades de procesamiento, mediante una arquitectura modular basada en nodos y mensajes. Gracias a ROS, es posible gestionar de manera eficiente la adquisición, procesamiento y distribución de datos de sensores, permitiendo el desarrollo de sistemas más robustos, escalables y reutilizables.

## 2. 🎯 Objetivos

- Familiarizarse con el uso e implementación de sensores.

- Comprender los principios de funcionamiento de diferentes tipos de sensores, así como sus implicaciones en sistemas de adquisición de datos.

- Evaluar la incertidumbre asociada a las mediciones obtenidas mediante sensores, aplicando métodos estadísticos básicos.

- Realizar el manejo de las plataformas robóticas disponibles a través del uso de ROS (Robot Operating System).

## 3. 🧰 Herramientas Necesarias

### 3.1. 🔭🛠️ Equipos

- Robot Lego EV3.
- Robot Kuboki.
- Computador.
- Lidar Hokuyo URG-04LX-UG01 con cable USB-mini y sensor RPLIDAR.
- Sensor de distancia por ultrasonido HC-SR04.
- Cinta métrica.
- Graduador o transportador, escuadra de 45° y 60°.
- Arduino UNO con cable USB-B.
- Protoboard.
- Cables de conexión para protoboard.


### 3.2. 🖥️💾 Software

- Ubuntu 20.04.
- Buscador web.
- Windows.
- [Software Hokuyo. URG Benri data viewing tool](https://drive.google.com/drive/folders/1ATOYSlWvBPTANnwIrI1PNbUlumYzaM3c?usp=drive_link).
- Matlab.
- Arduino IDE.
- Visual Studio Code.

## 4. 🔧➡️🚀 Procedimiento 


### 4.1. 🔍📚 Búsqueda bibliográfica

- ¿Qué es el Vocabulario Internacional de Metrología (VIM)?

- Según el VIM, defina los siguientes conceptos:

    - Exactitud de medida

    - Precisión de medida

    - Error de medida

    - Incertidumbre de medida

- Explique la diferencia entre un error sistemático y un error aleatorio.

- De acuerdo con la teoría estadística: ¿qué es el valor medio? ¿Qué magnitudes se utilizan para medir la dispersión de los datos?

- Busque una definición de que es ROS y sus principales ventajas

- Investigue sobre qué comandos se pueden usar con rosnode, rostopic, rosservice,rosmsg, rospack.

- Investigue acerca del robot TurtleBot2 y su relación con la base Kobuki.

- ¿Para que sirve los sensores cliff en el Kobuki?

- ¿Como leer un evento de dicho sensor?

- ¿Qué protocolo de comunicación usa el Lego Ev3 con sus sensores y actuadores?

- ¿Qué opciones de conexión permiten integrar sensores no nativos al sistema LEGO EV3?

### 4.2. Sensor HOKUYO

### 4.3. Sensor RPLIDAR

### 4.4. Sensor de ultrasonido

### 4.5. Sensores Lego

### 4.6. ROS
 
- Describa paso a paso que hacen los programas realizados en Python, indique las funciones de ROS
usadas.

-  Use turtle_teleop_key y el programa pysubpose.py para conocer las dimensiones del plano donde el Turtlesim puede moverse.

- Describa como usar algún servicio en Python. Luego pruebe el siguiente código ejemplo que se encarga de dibujar un cuadrado con el turtlesim: (se recomienda usar las instrucciones rosservice list y rosservice info)

### 4.7. ROS Kuboki

- Construya un archivo en Python que permita hacer la lectura de la información del sensor cliff y active
un sonido al ocurrir un evento con ese sensor. Active también el modo de teleoperación por teclado al
mismo tiempo para controlar el movimiento del Kobuki.

### 4.8. ROS Lego EV3



## 5. 📚🔗 Recursos

<details>
  <summary>🚗📡🌐 Sensores</summary>

- [Ultrasonic Sensor HC-SR04 and Arduino – Complete Guide](https://howtomechatronics.com/tutorials/arduino/ultrasonic-sensor-hc-sr04/)
- [Tutorial de Arduino y sensor ultrasónico HC-SR04](https://naylampmechatronics.com/blog/10_tutorial-de-arduino-y-sensor-ultrasonico-hc-sr04.html)
- [Medir distancia con Arduino y sensor de ultrasonidos HC-SR04](https://www.luisllamas.es/medir-distancia-con-arduino-y-sensor-de-ultrasonidos-hc-sr04/)

</details>

<details>
  <summary>🐢🤖 kobuki</summary>

</details>

<details>
  <summary>🧱🤖 Lego EV3 </summary>

</details>