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
  - [4.2. 👀🫲🏼👂🏼🤖🧠 Sensores](#42--sensores)
    - [4.2.1. 🔦👀🌐🔭 Sensor HOKUYO](#421--sensor-hokuyo)
    - [4.2.2. 🔦👀🌍📡 Sensor RPLIDAR](#422--sensor-rplidar)
    - [4.2.3. 🔊📡📏 Sensor de ultrasonido](#423--sensor-de-ultrasonido)
    - [4.2.4. 📡🧭🧱 Sensores Lego](#424--sensores-lego)
  - [4.3. 🌐🤖 ROS](#43--ros)
    - [4.3.1. 🗂️🌐🤖 Uso de ROS](#431-️-uso-de-ros)
    - [4.3.2. 🌐🐢🤖 ROS Kuboki](#432--ros-kuboki)
    - [4.3.3. 🌐🧱🤖 ROS Lego EV3](#433--ros-lego-ev3)
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
- Windows.
- [Software Hokuyo. URG Benri data viewing tool](./Recursos/Sensores/RPLidar/UrgBenriPlus_2.2.0(rev.274)_installer.exe).
- Matlab.
- Arduino IDE.
- Visual Studio Code.

## 4. 🔧➡️🚀 Procedimiento 


### 4.1. 🔍📚 Búsqueda bibliográfica

1. ¿Qué es el Vocabulario Internacional de Metrología (VIM)?

2. Según el VIM, defina los siguientes conceptos:

    - Exactitud de medida

    - Precisión de medida

    - Error de medida

    - Incertidumbre de medida

3. Explique la diferencia entre un error sistemático y un error aleatorio.

4. De acuerdo con la teoría estadística: ¿qué es el valor medio? ¿Qué magnitudes se utilizan para medir la dispersión de los datos?

5. Busque una definición de que es ROS y sus principales ventajas

6. Investigue sobre qué comandos se pueden usar con rosnode, rostopic, rosparam, rosservice, rosmsg y rospack.

7. Investigue acerca del robot TurtleBot2 y su relación con la base Kobuki.

8. ¿Para que sirve los sensores cliff en el Kobuki?

9. ¿Como leer un evento de dicho sensor?

10. ¿Qué protocolo de comunicación usa el Lego Ev3 con sus sensores y actuadores?

11. ¿Qué opciones de conexión permiten integrar sensores no nativos al sistema LEGO EV3?

### 4.2. 👀🫲🏼👂🏼🤖🧠 Sensores

<!--
>[!IMPORTANT]
>Puedes saltar estas secciones y con un bonus usar los sensores desde ROS
-->

#### 4.2.1. 🔦👀🌐🔭 Sensor HOKUYO

>[!CAUTION]
>Inicialmente no conecte el sensor al computador.

1. Instale, ejecute el software [URG Benri data viewing tool](./Recursos/Sensores/Hokuyo/UrgBenriPlus_2.2.0(rev.274)_installer.exe).
2. Realice la configuración del sensor y compuebe el funcionamiento adecuado del Lidar.
3. Abra MATLAB.
4. Desde MATLAB verificar con la instrucción `instrfind` que no hay puertos abiertos, la respuesta en la ventana de comandos debe ser: 

```matlab
  ans =

      []
```

>[!TIP]
>Si aparecen instrumentos asociados es preferible cerrar el software, desconectar el sensor, volver a abrir MATLAB y reconectar el sensor.

5. En la carpeta de trabajo con MATLAB copiar la carpeta [Lidar](./Recursos/Sensores/Lidar/).

```sh
# Con gitbash o linux puede usar estos comandos para copiar puede cambiar la primera linea y usar su directorio de trabajo
cd ~/Matlab 
git clone --filter=blob:none --no-checkout https://github.com/labsir-un/FRM_Lab_2_Sensores_y_ROS.git Lidar
cd Lidar
git sparse-checkout init
git sparse-checkout set Recursos/Sensores/Hokuyo
git checkout
mv Recursos/Sensores/Hokuyo/* ./
rm -r Recursos/
```

6. Abrir el Administrador de dispositivos (Windows) y conecte el sensor a un puerto USB, observe los cambios en la carpeta `Puertos COM y LPT`. Registre en número de puerto asignado al sensor.
7. Abra desde MATLAB el archivo [SetupLidar.m](./Recursos/Sensores/Lidar/SetupLidar.m) y modifique la línea 6 con el número de puerto `COM` correspondiente.
8. Organize su espacio de trabajo de manera que pueda colocar el sensor en 3 diferentes posturas en el área a mapear como el ejemplo mostrado a continuación con el sensor RPLidar.

<div align="center">
  <img src="https://imgur.com/jvpmgEM.png" alt="Montaje_sensor_RPLidar" width="600px">
</div>

9.  Establezca un punto de su área de trabajo y definalo como origen de coordenadas y defina direcciones **X** e **Y**.
10. Corra el programa `SetupLidar.m`.
11. Abra el programa [RunLidar2.m](./Recursos/Sensores/Lidar/RunLidar2.m).
12. Modifique el algoritmo para que haga 3 escaneos con separación de tiempo de 1 a 3 segundos entre ellos.
13. Coloque el sensor en la pose 1 mida y guarde los datos de esa pose  <picture> <source srcset="https://imgur.com/fHyzaJS.png" media="(prefers-color-scheme: dark)"> <source srcset="https://imgur.com/iL364wo.png" media="(prefers-color-scheme: light)">
    <img src="https://imgur.com/iL364wo.png" alt="Pose_1" width="60px">
</picture>.
1.  Corra el programa [RunLidar2.m](./Recursos/Sensores/Lidar/RunLidar2.m).
2.  Modifique el algoritmo en las líneas 11 y 16 para que genere una variable `LidarSet2`.
3.  Coloque el sensor en la pose 2 mida y guarde los datos de esa pose <picture> <source srcset="https://imgur.com/x7fDgUo.png" media="(prefers-color-scheme: dark)"> <source srcset="https://imgur.com/y0JthnJ.png" media="(prefers-color-scheme: light)">
    <img src="https://imgur.com/y0JthnJ.png" alt="Pose_2" width="60px">
</picture>.
4.  Corra el programa [RunLidar2.m](./Recursos/Sensores/Lidar/RunLidar2.m).
5.  Modifique el algoritmo en las líneas 11 y 16 para que genere una variable `LidarSet3`.
6.  Coloque el sensor en la pose 3 mida y guarde los datos de esa pose <picture> <source srcset="https://imgur.com/QCEb8Ri.png" media="(prefers-color-scheme: dark)"> <source srcset="https://imgur.com/kVoWPrg.png" media="(prefers-color-scheme: light)">
    <img src="https://imgur.com/kVoWPrg.png" alt="Pose_3" width="60px">
</picture>.
7.  Corra el programa [RunLidar2.m](./Recursos/Sensores/Lidar/RunLidar2.m).
8.  Desconecte el lidar usando el programa [DisconnectLidar.m](./Recursos/Sensores/Hokuyo/DisconnectLidar.m)
9.  Presente la foto de su área de trabajo modificada con las dimensiones totales y la pose aproximada del sensor en cada conjunto de medidas.
10. Para cada pose informe los datos $[x, y, θ]_{i}$ y presente los datos capturados con alguno de los métodos plot(scan) presentados en la página de ayuda de [MATLAB: lidarScan Create object for storing 2-D lidar scan](https://la.mathworks.com/help/nav/ref/lidarscan.html).
11. Para cada pose presente los datos en forma de mapa de ocupación. Ayuda de [MATLAB occupancyMap Create 2-D occupancy map](https://la.mathworks.com/help/nav/ref/occupancymap.html) ejemplo [Insert Laser Scans into Occupancy Map](https://la.mathworks.com/help/nav/ref/occupancymap.insertray.html).
12. Usando los datos capturados en las 3 poses construya un mapa de ocumación de su área de trabajo, use como referencia la ayuda de [MATLAB: buildMap Build occupancy map from lidar scans](https://la.mathworks.com/help/nav/ug/build-occupancy-map-from-lidar-scans-and-poses.html).
13. Realice un análisis de los errores y fuentes de error evidenciados en la construcción del mapa en el punto anterior.

#### 4.2.2. 🔦👀🌍📡 Sensor RPLIDAR

1. Organize su espacio de trabajo de manera que pueda colocar el sensor en 3 diferentes posturas en el área a mapear como aparece a continuación.
2.  Establezca un punto de su área de trabajo y definalo como origen de coordenadas y defina direcciones **X** e **Y**.
3. Realice una toma de datos similar a la realizada para el sensor Hokuyo. Utilice los algoritmos disponibles en la carpeta [RPLidar](./Recursos/Sensores/RPLidar).
>[!TIP]
>No olvide cambiar el número de puerto `COM` en los scripts
4. Realice el mismo post-procesamiento de datos que el realizado con el sensor Hokuyo (Pasos 22-26).

#### 4.2.3. 🔊📡📏 Sensor de ultrasonido

1. En los sitios referenciados en la sección [5. 📚🔗 Recursos](#5--recursos) identifique la forma de conectar el ARDUINO y el sensor [HC-SR04](./Recursos/Sensores/Ultra_Sonido/HCSR04.pdf) y la forma de conexión a su computador. Haga las conexiones correspondientes. Tenga en cuenta los números de pines del ARDUINO a los cuales conectó los pines de trigger y de echo del HCSR04.
2. Abra el IDE de Arduino y cargue el archivo [usound3.ino](./Recursos/Sensores/Ultra_Sonido/usound3.ino). Modifique las líneas correspondientes para que coincidan con los pines del Arduino que se están utilizando en su configuración actual.

```cpp
const int pinecho = 11;
const int pintrigger = 12;
```

3. Compila el código y súbelo al Arduino mediante el entorno de desarrollo (IDE) de Arduino.
4. Desde el IDE de Arduino, abra el monitor serial para comprobar que los datos se están leyendo y registrando adecuadamente. Una vez verificado, cierra el monitor.
5. Instale el montaje experimental de acuerdo con el esquema mostrado.

<div align="center">
  <img src="https://imgur.com/0nEB0bk.png" alt="Montaje_sensor_UltraSonido" width="600px">
</div>

6. En MATLAB abra el archivo [ultrasound3.m](./Recursos/Sensores/Ultra_Sonido/ultrasound3.m).
7. En la ventana de comandos, utiliza la instrucción `serialportlist` para identificar el puerto asignado al Arduino.
8. Edita la instrucción `port = serialport()` en el archivo, configurando el puerto `COM` que corresponda al asignado para el Arduino. El programa leerá los datos recibidos por el puerto serie y los almacenará en la variable `dist`.
9.  Ubica un objeto (por ejemplo, una caja de cartón o una tabla pequeña) que actúe como referencia para realizar la medición de distancia.
10. Coloca el objeto a una distancia de 1 metro del sensor, verifica la distancia utilizando una cinta métrica y registra el valor obtenido.
11. Ejecuta el programa [ultrasound3.m](./Recursos/Sensores/Ultra_Sonido/ultrasound3.m) para realizar la medición de distancia y guarda los resultados obtenidos en el proceso en un archivo debidamente identificado.
12. Repita los dos pasos anteriores en tres posiciones adicionales del objeto, asegurándose de que las distancias al sensor estén entre 1 y 2,5 metros.
13. Para cada conjunto de datos, calcule la distancia media, la desviación estándar, el error absoluto y el error relativo en relación con la medición de distancia realizada con el flexómetro.
14. Presente la gráfica de distancia en función del índice de muestra.
15. Para cada distancia medida, incluya un histograma que muestre la distribución de los datos.
16. Incluya gráficas que representen el comportamiento de la desviación estándar, el error absoluto y el error relativo en relación con la distancia media.
17. Lleve a cabo los análisis necesarios y elabore las conclusiones correspondientes.

#### 4.2.4. 📡🧭🧱 Sensores Lego

Llevar a cabo una estimación preliminar de la incertidumbre de medida en los sensores y actuadores utilizados en los kits LEGO EV3.

1. Programe el robot LEGO EV3 para realizar las siguientes acciones: arranque, desplazamiento en línea recta de 100 cm y detención. Configure la velocidad de desplazamiento al 30% de la velocidad máxima del robot. Registre los datos de posición al inicio y al final del trayecto utilizando los siguientes elementos:

   1. Encoder sensor de rueda.
   2. Sensor de Ultrasonido del EV3.
   3. Cinta métrica.

2. Repita el procedimiento anterior, pero ahora con la velocidad al 100 % de la máxima.

3. Realice un anális comparativo de las medidas y calcule los errores de desplazamiento tomando como patrón la cinta métrica.

4. Diseñe e implemente un algoritmo que permita girar una rueda del robot LEGO EV3 en intervalos de 30° y 45°. Configure un montaje experimental que permita medir externamente los ángulos girados utilizando un método alternativo, como un transportador, un apuntador láser con cinta métrica, u otro sistema de referencia. Realice múltiples repeticiones de la medición para evaluar la precisión del sistema.

5. Realice un análisis comparativo entre los valores de desplazamiento angular medidos por el sistema LEGO EV3 y los obtenidos mediante el método de medición externo. Utilice este último como patrón de referencia para calcular los errores de desplazamiento. Determine el error absoluto, el error relativo y, si es pertinente, el error porcentual para evaluar la precisión del sistema.

### 4.3. 🌐🤖 ROS

#### 4.3.1. 🗂️🌐🤖 Uso de ROS

>[!IMPORTANT]
>Si quiere saber más de como funciona ROS, su estructura y como se estructura un paquete vea [📚🌐🤖 Introducción a ROS](https://github.com/labsir-un/FRM_Lab_0_Intro_software/blob/main/Archivos/ROS/Recursos/Introduccion.md).

1. Cree un Workspace para los archivos. En el siguiente ejemplo se crea uno con el nombre `catkin_ws`.

```sh 
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```
 
2. Clone el paquete `laboratorio_2` de este respositorio para esto use los siguientes comandos:

```sh
cd ~/catkin_ws/src
git clone --filter=blob:none --no-checkout https://github.com/labsir-un/FRM_Lab_2_Sensores_y_ROS.git laboratorio_2
cd laboratorio_2
git sparse-checkout init
git sparse-checkout set Recursos/ROS/laboratorio_2
git checkout
mv Recursos/ROS/laboratorio_2/* ./
rm -r Recursos/
```

3. Complilar el Workspace y cargar configuraciones.

```sh
cd ~/catkin_ws
#Compila todo el workspace creado
catkin_make
#Carga todas las configuraciones necesarias en el entorno actual
source devel/setup.bash
```

4. Dar permisos de ejecución a los scripts de python.

```sh
chmod +x ~/catkin_ws/src/laboratorio_2/scripts/*.py
```

5. Abra otra terminal e inicie ROS.

```sh
roscore
```

6. Abra una tercera terminal e inicie el nodo de `turtlesim`.

```sh
rosrun turtlesim turtlesim_node
```

7. En la primera terminal corra el ejecutable de [hello.cpp](./Recursos/ROS/laboratorio_2/src/hello.cpp). Con esto se correra el primer archivo ejecutable de C++.

```sh
rosrun laboratorio_2 hello
```

8. Corra el ejecutable de [subpose.cpp](./Recursos/ROS/laboratorio_2/src/subpose.cpp). Este programa se suscribe a la pose de la tortuga y la muestra en la terminal.

```sh
rosrun laboratorio_2 subpose
```

9. Corra el ejecutable de [pubvel.cpp](./Recursos/ROS/laboratorio_2/src/pubvel.cpp). Este programa publica en las velocidades de la tortuga con valores alatorios lo cual hace que se mueva en la escena.

```sh
rosrun laboratorio_2 pubvel
```

10.  Corra el ejecutable de [pysubpose.py](./Recursos/ROS/laboratorio_2/scripts/pysubpose.py). Este programa se suscribe a la pose de la tortuga y la muestra en la terminal.

```sh
rosrun laboratorio_2 pysubpose.py
```

11. Corra el ejecutable de [pypubvel.py](./Recursos/ROS/laboratorio_2/scripts/pypubvel.py). Este programa publica en las velocidades de la tortuga con valores alatorios lo cual hace que se mueva en la escena.

```sh
rosrun laboratorio_2 pypubvel.py
```

12. Detenga el nodo de `turtlesim` y lance varios nodos usando el archivo [p.launch](./Recursos/ROS/laboratorio_2/launch/p.launch).

```sh
roslaunch laboratorio_2 p.launch
```

13. Describa paso a paso que hacen los programas realizados en Python, indique las funciones de ROS usadas.

14. Use `turtle_teleop_key` y el programa `pysubpose.py` para conocer las dimensiones del plano donde el Turtlesim puede moverse.

15. Describa como usar algún servicio en Python.

16. Pruebe el código ejemplo [pycuadrado.py](./Recursos/ROS/laboratorio_2/scripts/pycuadrado.py) que se encarga de dibujar un cuadrado con el turtlesim. Y revise como se usan servicios en este script.

>[!Note]
>Se recomienda usar las instrucciones `rosservice list` y `rosservice info` para ver los servicios que hay disponibles y la información de estos.

17.  Inicie un nodo de `turtlesim`, utilice el servicio `spawn` para generar una segunda tortuga y desarrolle un programa en Python que permita a ambas tortugas dibujar un triángulo y un cuadrado. Emplee un archivo `launch` para automatizar la ejecución de la tarea.

#### 4.3.2. 🌐🐢🤖 ROS Kuboki

1. Desarrolle un programa que permita realizar la lectura del sensor de acantilado (cliff) del robot Kobuki y reproduzca un sonido al detectarse un evento asociado a dicho sensor. De forma simultánea, habilite el modo de teleoperación mediante teclado para controlar el movimiento del robot.

#### 4.3.3. 🌐🧱🤖 ROS Lego EV3

1. Desarrolle un programa que permita realizar la lectura de los siguientes sensores: táctil, giroscopio y, adicionalmente, un sensor infrarrojo, ultrasónico o de color, con el objetivo de detectar eventos asociados a cualquiera de ellos. Simultáneamente, implemente un modo de teleoperación, ya sea mediante teclado o una interfaz gráfica (GUI), para controlar el movimiento del robot.

2. Con las lecturas o eventos del robot genere una rutina como: parada con un umbral de seguridad, control de giro o generación de sonido. 

## 5. 📚🔗 Recursos

<details>
  <summary>🚗📡 Sensores</summary>

- [Lidar Technologies 101](https://www.youtube.com/watch?v=3EehCU3csJQ)
- [Ultrasonic Sensor HC-SR04 and Arduino – Complete Guide](https://howtomechatronics.com/tutorials/arduino/ultrasonic-sensor-hc-sr04/)
- [Tutorial de Arduino y sensor ultrasónico HC-SR04](https://naylampmechatronics.com/blog/10_tutorial-de-arduino-y-sensor-ultrasonico-hc-sr04.html)
- [Medir distancia con Arduino y sensor de ultrasonidos HC-SR04](https://www.luisllamas.es/medir-distancia-con-arduino-y-sensor-de-ultrasonidos-hc-sr04/)
- [Tracker](https://opensourcephysics.github.io/tracker-website/)
- [Comparaison protocoles communication i2c spi uart](https://www.parlezvoustech.com/en/comparaison-protocoles-communication-i2c-spi-uart/)
</details>


<details>
  <summary>🌐🤖 ROS</summary>

- [ROSwiki kobuki](http://wiki.ros.org/kobuki/Tutorials)
- [ROSwiki tutoriales](https://wiki.ros.org/ROS/Tutorials)
- [Aprender ROS. #1.1 ¿Qué necesitas para empezar?](https://www.youtube.com/watch?v=gcLbsIMBZR4)
- [[ROS Spanish Tutorials] ROS Básico en 5 días #Chapter 0 - part 1](https://www.youtube.com/watch?v=cAnMkvXy2hw)

</details>

<details>
  <summary>🐢🤖 kobuki</summary>

- [ROSwiki kobuki](http://wiki.ros.org/kobuki/Tutorials)
- [Kobuki TurtleBot + ROS + Jetson TX2](https://www.youtube.com/watch?v=gRBA-EC6COU)
- [Guia de uso del robot Kobuki mediante ROS](https://github.com/labsir-un/FRM_Lab_0_Intro_software/blob/main/Archivos/ROS/Recursos/Kuboki.md)
</details>

<details>
  <summary>🧱🤖 Lego EV3 </summary>
 
 - [ROSwiki EV3](https://wiki.ros.org/Robots/EV3)
 - [ROS Robot With Lego EV3 and Docker](https://www.instructables.com/ROS-Robot-With-Lego-EV3-and-Docker/)
 - [Lego NXT](https://robots.ros.org/lego-nxt/)
 - [Ros And Wiimote](https://www.ev3dev.org/projects/2017/02/05/ROS-and-wiimote/)
 - [Connecting the EV3 and the Arduino](https://www.dexterindustries.com/howto/connecting-ev3-arduino/)
 - [Conectando ROS y EV3 mediante Arduin](https://github.com/FCruzV10/ROSEV3)
 - [Conexión de Lego mindstorms EV3 con ROS por medio de comunicación MQTT y el sistema ev3dev](https://github.com/JSDaleman/ev3_mqtt_ros)
- [Mobile Robotic developement Platform interfacing ROS and EV3](https://www.youtube.com/watch?v=iRQqEKYDRI4)
</details>
