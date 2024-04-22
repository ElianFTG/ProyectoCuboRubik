# ProyectoCuboRubik
1. **Autor:** Elian Franco Tito Gusman
2. **Descripcion del proyecto**
    Este proyecto se centra en el desarrollo de un sistema inteligente que puede resolver un Cubo de Rubik utilizando algoritmos de estructura de datos. El objetivo principal es diseñar e implementar algoritmos eficientes que puedan resolver el Cubo de Rubik en el menor número de movimientos posible.

3. **Requerimientos del entorno de programación**
    En el proyecto se utilizara como entorno de programacion Visual Studio Code con el lenguaje python, se utilizara librerias las librerias Count y Numpy tanto para validaciones y manipulaciones del obejto Cubo Rubik

4. **Manual de uso**
    1. **Formato de carga del cubo para un archivo de texto** \
        El formato de carga correcta es el siguiente:

        color color color \
        color color color \
        color color color \
        ... \
        ... \
        ... 

        sucesivamente continuando con la siguiente cara, cada cara debe estar con 3 filas y 3 columnas
        el orden para insertar las caras es arriba,frente, izquierda,derecha, atras, abajo.
        Los colores centrales estan definidos por ende para las caras tendran que tener los siguientes colores centrales: superior(blanco), frontal(verde), izquierda(naranja),derecha(rojo), atras(azul), abajo(amarillo)
        sobra decir que tambien cada color debe repetirse 9 veces solamente: \
        Ejemplo: \
        blanco blanco blanco\
        blanco blanco blanco\
        blanco blanco blanco\
        verde verde verde\
        verde verde verde\
        verde verde verde\
        naranja naranja naranja\
        naranja naranja naranja\
        naranja naranja naranja\
        rojo rojo rojo\
        rojo rojo rojo\
        rojo rojo rojo\
        azul azul azul\
        azul azul azul\
        azul azul azul\
        amarillo amarillo amarillo\
        amarillo amarillo amarillo\
        amarillo amarillo amarillo\
    
    2. **.Instrucciones para ejecutar el programa**
        El programa principal el archivo que tiene por nombre "main.cpp".
        la unica interaccion con el usuario es a traves de la consola donde unicamente debera ingresar la direccion total del archivo para cargar el Cubo y se ejecutara el programa de resolucion del cubo que se inserto, terminando, lanzara los resultados de movimientos adecuados para la resolucion

5. **Diseño e implementación**
    1. **descripción de modelo del problema** \
    Para el diseño estructural del cubo, se penso en como dividir las caras al mismo tiempo las caras son una matriz 3x3, para insertar con un archivo de texto, se pensó utilizar una
    lista que cubra las caras que usaremos para un mejor entendimiento y manejo de cambios, en el codigo podemos observar que se hace mucha alucion al tema de punteros ya que en python indirectamente todo elemento es un puntero y al cambiar en cualquier el valor, se cambiara en todo lo que este igualado a esa variable instanciada por primera vez.
    Se aplicaron como 4 restricciones, 2 al momento de insertar con un archivo y otras 2 en la evaluacion del cubo insertado, no se tomó en cuenta la restriccion de adyacencias.
    Tambien se utilizaron las librerias Numpy y Count(collections), para una mejor manipulacion, comparacion en matrices y auxiliar en el control de datos
    2. **Algoritmo utilizado** \
    Se utilizo el algoritmo de Busqueda en Amplitud (BFS) ya que en la comprension de los diferentes estados del cubo, no se sabe con exactitud que movimiento puede ser el mas optimo
    asumiendo que desconocemos de los algoritmos tradicionales para su resolucion, asumiendo esto, me dejó en la conclusion de que la unica manera posbile para esto es aplicando todos los estados posibles e ir comparando con un cubo que ya este resuelto.
    3. **Promps utilizados para la codificacion**\
    Para una codificacion mas sencilla se utilizo 3 promps consultados a ChatGPT:\
    **"Crea una funcion que reciba como parametro una matriz y lo gire 90 grados en sentido antihorario"** \
    Resultado:
    ```
    def girar_matriz_90_anti(matriz):
    # Obtenemos las dimensiones de la matriz original
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Creamos una matriz vacía para almacenar la matriz girada
    matriz_girada = [[0] * filas for _ in range(columnas)]
    
    # Giramos la matriz 90 grados en sentido antihorario
    for i in range(filas):
        for j in range(columnas):
            matriz_girada[columnas - 1 - j][i] = matriz[i][j]
    
    return matriz_girada
    ```
    ***"crea una funcion que reciba como parametro una matriz y lo gire 90 grados en sentido horario"*** \
    Resultado:
    ```
    def giro_horario(self, matrix):
        transposed_matrix = list(zip(*matrix))
        rotated_matrix = [list(row[::-1]) for row in transposed_matrix]
        return rotated_matrix
    ```
    ***"Como comparo la igualdad entre 2 objetos de una misma clase"***\
    Resultado:
    ```
    def __eq__(self, otro):
        if isinstance(otro, MiClase):
            return self.valor == otro.valor
        return False
    ```
6. **Trabajo futuro**
    - Refactory: Para esta primera version, se tiene mucho codigo repetido en los movimientos del cubo, por ello, puede se puede mejorar la legibilidad y la estructura de codigo.
    - Una mejor estructura de datos posible: Se podria aplicar una estructura de datos que requiera de Heuristica como A*(A star) como una mejor solucion en dado caso de que ignoremos un poco la condicion de desconocimiento de algoritmos tipicos de armado, ya que podemos aplicar la heuristica a cada estado de que tan lejos puede estar a uno de los [7 estados condicionales para el armado tipico de un cubo](https://rubikscu.be/#tutorial)
    - Crear diseño de interfaz grafica: Se podria aplicar una mejor interaccion con el usuario y visualizacion para el usuario agregando una interfaz 3D

    