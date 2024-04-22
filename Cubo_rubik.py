from collections import Counter
import numpy as np

class CuboRubik:  
    def __init__(self,arriba=np.zeros((3, 3),dtype=object), 
                 frente=np.zeros((3, 3), dtype=object), 
                 izquierda=np.zeros((3, 3), dtype=object), 
                 derecha=np.zeros((3, 3), dtype=object),
                 atras=np.zeros((3, 3), dtype=object),
                 abajo=np.zeros((3, 3), dtype=object)
                 ):
        self.cubo = np.array([arriba,frente,izquierda,derecha,atras,abajo])
        self.arriba = self.cubo[0]
        self.frente = self.cubo[1]
        self.izquierda = self.cubo[2]
        self.derecha= self.cubo[3]
        self.atras = self.cubo[4]
        self.abajo = self.cubo[5]
        
        self.valido = False

    def mostrar_sector(self, lado):
        for i in range(len(lado)):
            for j in range(len(lado[i])):
                print(lado[i][j], end=" ")
            print()
        print("-----------------------")

    

    def mostrar_cubo(self):
        print('arriba')
        self.mostrar_sector(self.arriba)
        print('frente')
        self.mostrar_sector(self.frente)
        print('izquierda')
        self.mostrar_sector(self.izquierda)
        print('derecha')
        self.mostrar_sector(self.derecha)
        print('atras')
        self.mostrar_sector(self.atras)
        print('abajo')
        self.mostrar_sector(self.abajo)

    def validacion_centros(self):
        centros = ["blanco", "verde","naranja","rojo","azul","amarillo"]
        centros_incertados =  [centro[1][1].lower() for centro in self.cubo]
        if centros == centros_incertados:
            return True
        print("Los centros no son validos")
        return False 

    def validacion_colores(self):
        colores = [casilla for cara in self.cubo for filas in cara for casilla in filas]
        colores_contados = Counter(colores).most_common()
        if colores_contados[0][1] == colores_contados[5][1]:
            return True
        print("Hay por lo menos un color de mas o menos")
        return False 

    
        

    def validacion_cubo(self):
        self.valido = self.validacion_centros() and self.validacion_colores()

    def __eq__(self, otro_objeto):
        if isinstance(otro_objeto, CuboRubik):
            arriba = np.array_equal(self.arriba,otro_objeto.arriba)
            frente = np.array_equal(self.frente,otro_objeto.frente)
            izquierda = np.array_equal(self.izquierda,otro_objeto.izquierda)
            derecha = np.array_equal(self.derecha,otro_objeto.derecha)
            atras = np.array_equal(self.atras,otro_objeto.atras)
            abajo = np.array_equal(self.abajo,otro_objeto.abajo)
            return arriba and frente and izquierda and derecha and atras and abajo

    def insertar_datos_cubo(self,txt):
        recorrido_caras = -1
        with open(txt, 'r') as f:
            lineas = f.readlines()
        tamanio = len(lineas)
        if tamanio == 18:
            for indice in range(tamanio):
                division_espacios = lineas[indice].split()
                if len(division_espacios) == 3:
                    if indice % 3 == 0:
                        recorrido_caras += 1
                        casillas_cubo = 0
                    self.cubo[recorrido_caras][casillas_cubo] = division_espacios
                    casillas_cubo += 1
                else:
                    print("Error, hay mas de 3 elementos o menos, en una fila")
                    return
        else:
            print("Error en insertar valores, no es cubo 3x3")
            return
        self.validacion_cubo()

    def copiar_elementos(self):
        nuevo = CuboRubik(self.arriba,self.frente,self.izquierda,self.derecha,self.atras,self.abajo)
        return nuevo 
    

    def giro_horario(self, matrix):
        transposed_matrix = list(zip(*matrix))
        rotated_matrix = [list(row[::-1]) for row in transposed_matrix]
        return rotated_matrix
    

    def giro_antihorario(self,matrix):
        filas = len(matrix)
        columnas = len(matrix[0])
        # Creamos una matrix vacía para almacenar la matrix girada
        matrix_girada = [[0] * filas for _ in range(columnas)]
        # Giramos la matrix 90 grados en sentido antihorario
        for i in range(filas):
            for j in range(columnas):
                matrix_girada[columnas - 1 - j][i] = matrix[i][j]

        return matrix_girada


    def Up(self):
        frente = self.frente[0].copy()
        derecha = self.derecha[0].copy()
        atras = self.atras[0].copy()
        izquierda = self.izquierda[0].copy()
        self.frente[0] = derecha
        self.derecha[0] = atras
        self.atras[0] = izquierda
        self.izquierda[0] = frente
        self.arriba = self.giro_horario(self.arriba)
        
    def Front(self):
        columnas_ady_U = [ self.arriba[2][columna] for columna in range(3) ]
        columnas_ady_D = [ self.abajo[0][columna] for columna in range(3) ]
        filas_ady_R = [self.derecha[filas][0] for filas in range(3) ][::-1]
        filas_ady_L = [self.izquierda[filas][2] for filas in range(3) ][::-1]
        self.arriba[2] = filas_ady_L
        self.abajo[0] = filas_ady_R
        for i in range(3):
            self.izquierda[i][2] = columnas_ady_D[i]
            self.derecha[i][0] = columnas_ady_U[i]

        self.frente = self.giro_horario(self.frente)
        
    def columnas_laterales(self, matrizes,posicion_columna_AFA,posicion_columna_D):
        columnas = []
        #[arriba,frente,abajo,atras]
        for matriz in range(3):
            columnas.append([ matrizes[matriz][filas][posicion_columna_AFA] for filas in range(3)])
                
        columnas.append([matrizes[3][filas][posicion_columna_D] for filas in range(3)])
        return columnas

    def Left(self):
        columnas = self.columnas_laterales([self.arriba,self.frente,self.abajo,self.atras],0,2)
        columnas[3] = columnas[3][::-1]
        columnas[2] = columnas[2][::-1]
        for filas in range(3):
          self.arriba[filas][0] = columnas[3][filas]
          self.frente[filas][0] = columnas[0][filas]
          self.abajo[filas][0] = columnas[1][filas]
          self.atras[filas][2] = columnas[2][filas]
        self.izquierda = self.giro_horario(self.izquierda)

    def Right(self):
        columnas = self.columnas_laterales([self.arriba,self.frente,self.abajo,self.atras],2,0)
        columnas[0] = columnas[0][::-1]
        columnas[3] = columnas[3][::-1]
        
        #[arriba,frente,abajo,atras]
        for filas in range(3):
          self.arriba[filas][2] = columnas[1][filas]
          self.frente[filas][2] = columnas[2][filas]
          self.abajo[filas][2] = columnas[3][filas]
          self.atras[filas][0] = columnas[0][filas]
        self.derecha = self.giro_horario(self.derecha)
        
    def Back(self):
        columnas_ady_U = [ self.arriba[0][columna] for columna in range(3) ][::-1]
        columnas_ady_D = [ self.abajo[2][columna] for columna in range(3) ][::-1]
        filas_ady_R = [self.derecha[filas][2] for filas in range(3) ]
        filas_ady_L = [self.izquierda[filas][0] for filas in range(3) ]
        self.arriba[0] = filas_ady_R
        self.abajo[2] = filas_ady_L
        for i in range(3):
            self.izquierda[i][0] = columnas_ady_U[i]
            self.derecha[i][2] = columnas_ady_D[i]

        self.atras = self.giro_horario(self.atras)
    
    def Down(self):
        frente = self.frente[2].copy()
        derecha = self.derecha[2].copy()
        atras = self.atras[2].copy()
        izquierda = self.izquierda[2].copy()
        self.frente[2] = izquierda
        self.derecha[2] = frente
        self.atras[2] = derecha
        self.izquierda[2] = atras
        self.abajo = self.giro_horario(self.abajo)
        

    # Funciones de giro en sentido antihorario
    def Up_prima(self):
        frente = self.frente[0].copy()
        derecha = self.derecha[0].copy()
        atras = self.atras[0].copy()
        izquierda = self.izquierda[0].copy()
        self.frente[0] = izquierda
        self.derecha[0] = frente
        self.atras[0] = derecha
        self.izquierda[0] = atras
        self.arriba = self.giro_antihorario(self.arriba)      


    def Front_prima(self):
        columnas_ady_U = [ self.arriba[2][columna] for columna in range(3) ][::-1]
        columnas_ady_D = [ self.abajo[0][columna] for columna in range(3) ][::-1]
        filas_ady_R = [self.derecha[filas][0] for filas in range(3) ]
        filas_ady_L = [self.izquierda[filas][2] for filas in range(3) ]
        self.arriba[2] = filas_ady_R
        self.abajo[0] = filas_ady_L
        for i in range(3):
            self.izquierda[i][2] = columnas_ady_U[i]
            self.derecha[i][0] = columnas_ady_D[i]
        self.frente = self.giro_antihorario(self.frente)
        
    def Back_prima(self):
        columnas_ady_U = [ self.arriba[0][columna] for columna in range(3) ]
        columnas_ady_D = [ self.abajo[2][columna] for columna in range(3) ]
        filas_ady_R = [self.derecha[filas][2] for filas in range(3) ][::-1]
        filas_ady_L = [self.izquierda[filas][0] for filas in range(3) ][::-1]
        self.arriba[0] = filas_ady_L
        self.abajo[2] = filas_ady_R
        for i in range(3):
            self.izquierda[i][0] = columnas_ady_D[i]
            self.derecha[i][2] = columnas_ady_U[i]
        self.atras = self.giro_antihorario(self.atras)        

    def Left_prima(self):
        columnas = self.columnas_laterales([self.arriba,self.frente,self.abajo,self.atras],0,2)
        #[arriba,frente,abajo,atras]
        columnas[0] = columnas[0][::-1]
        columnas[3] = columnas[3][::-1]
        for filas in range(3):
          self.arriba[filas][0] = columnas[1][filas]
          self.frente[filas][0] = columnas[2][filas]
          self.abajo[filas][0] = columnas[3][filas]
          self.atras[filas][2] = columnas[0][filas]
        self.izquierda = self.giro_antihorario(self.izquierda)

    def Right_prima(self):
        columnas = self.columnas_laterales([self.arriba,self.frente,self.abajo,self.atras],2,0)
        columnas[2] = columnas[2][::-1]
        columnas[3] = columnas[3][::-1]
        
        #[arriba,frente,abajo,atras]
        for filas in range(3):
          self.arriba[filas][2] = columnas[3][filas]
          self.frente[filas][2] = columnas[0][filas]
          self.abajo[filas][2] = columnas[1][filas]
          self.atras[filas][0] = columnas[2][filas]
        self.derecha = self.giro_antihorario(self.derecha)

    def Down_prima(self):
        frente = self.frente[2].copy()
        derecha = self.derecha[2].copy()
        atras = self.atras[2].copy()
        izquierda = self.izquierda[2].copy()
        self.frente[2] = derecha
        self.derecha[2] = atras
        self.atras[2] = izquierda
        self.izquierda[2] = frente
        self.abajo = self.giro_antihorario(self.abajo) 

    def girar_pieza(self, sentido):
        if sentido == "Up":
            self.Up()
        elif sentido == "Right":
            self.Right()
        elif sentido == "Left":
            self.Left()
        elif sentido == "Front":
            self.Front()
        elif sentido == "Back":
            self.Back()
        elif sentido == "Down":
            self.Down()
        elif sentido == "Up'":
            self.Up_prima()
        elif sentido == "Right'":
            self.Right_prima()
        elif sentido == "Left'":
            self.Left_prima()
        elif sentido == "Front'":
            self.Front_prima()
        elif sentido == "Back'":
            self.Back_prima()
        elif sentido == "Down'":
            self.Down_prima()