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
  - [4.6. ROS Kuboki](#46-ros-kuboki)
  - [4.7. ROS Lego EV3](#47-ros-lego-ev3)
- [5. 📚🔗 Recursos](#5--recursos)


</details>

---

<h1> 👁️🧠🤖 Guía 2: Introducción al uso de sensores y ROS </h1>

## 1. 📖 Introducción

Los sensores son elementos básicos para que los robots móviles cumplan con su función. Los sensores tienen un conjunto de características técnicas, se clasifican en características estáticas y características dinámicas. Dentro de estas características o asociadas a ellas hay un conjunto de valores de error que conforman la incertidumbre de medida.

En la medida que deseamos mejor desempeño de los robots, esos errores se hacen evidentes o cobran mayor importancia. Reconocer la existencia, magnitud y comportamiento de los errores nos permite hacer un control de esos errores mediante pre-procesamineto de señales o al menos identificar porqué el comportamiento de los robots es diferente al esperado.

## 2. 🎯 Objetivos

- Familiarizarse con el uso e implementación de sensores en entornos de medición.

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
- Microcontrolador Arduino con cable USB-B.
- Protoboard.
- Cables de conexión para protoboard.


### 3.2. 🖥️💾 Software

- Ubuntu 20.04.
- Buscador web.
- Windows.
- [Software Hokuyo. URG Benri data viewing tool](https://drive.google.com/drive/folders/1ATOYSlWvBPTANnwIrI1PNbUlumYzaM3c?usp=drive_link)
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

### 4.2. Sensor HOKUYO

### 4.3. Sensor RPLIDAR

### 4.4. Sensor de ultrasonido

### 4.5. Sensores Lego

### 4.6. ROS

### 4.7. ROS Kuboki

- Realice una investigación acerca del robot TurtleBot2 y su relación con la base Kobuki.
- ¿Para que sirve los sensores cliff en el Kobuki?¿Como leer un evento de dicho sensor?
- Construya un archivo en Python que permita hacer la lectura de la información del sensor cliff y active
un sonido al ocurrir un evento con ese sensor. Active también el modo de teleoperación por teclado al
mismo tiempo para controlar el movimiento del Kobuki.

### 4.8. ROS Lego EV3



## 5. 📚🔗 Recursos

<details>
  <summary>🐢🤖 kobuki</summary>

</details>

<details>
  <summary>🧱🤖 Lego EV3 </summary>

</details>