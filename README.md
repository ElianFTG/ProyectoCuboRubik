# ProyectoCuboRubik
1. **Autor:** Elian Franco Tito Gusman
2. **Descripcion del proyecto**
    Este proyecto se centra en el desarrollo de un sistema inteligente que puede resolver un Cubo de Rubik utilizando algoritmos de estructura de datos. El objetivo principal es diseñar e implementar algoritmos eficientes que puedan resolver el Cubo de Rubik en el menor número de movimientos posible.

3. **Requerimientos del entorno de programación**
    En el proyecto se utilizara como entorno de programacion Visual Studio Code con el lenguaje python, se utilizara librerias las librerias Count y Numpy tanto para validaciones y manipulaciones del obejto Cubo Rubik

4. **Manual de uso**
    1. **Formato de carga del cubo para un archivo de texto**
        El formato de carga correcta es el siguiente:

        color color color
        color color color
        color color color
        ...
        ...
        ...

        sucesivamente continuando con la siguiente cara, cada cara debe estar con 3 filas y 3 columnas
        el orden para insertar las caras es arriba,frente, izquierda,derecha, atras, abajo.
        Los colores centrales estan definidos por ende para las caras tendran que tener los siguientes colores centrales: superior(blanco), frontal(verde), izquierda(naranja),derecha(rojo), atras(azul), abajo(amarillo)
        sobra decir que tambien cada color debe repetirse 9 veces solamente
    
    2. **.Instrucciones para ejecutar el programa**
        El programa principal el archivo que tiene por nombre "main.cpp".
        la unica interaccion con el usuario es a traves de la consola donde unicamente debera ingresar la direccion total del archivo para cargar el Cubo y se ejecutara el programa de resolucion del cubo que se inserto

    