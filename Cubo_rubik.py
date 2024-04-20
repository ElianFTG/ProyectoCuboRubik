import copy

class CuboRubik:
    # def __init__(self):
    #     self.arriba = [[]*3, []*3, []*3]
    #     self.frente = [[]*3, []*3, []*3]
    #     self.izquierda = [[]*3, []*3, []*3]
    #     self.derecha= [[]*3, []*3, []*3]
    #     self.abajo = [[]*3, []*3, []*3]
    #     self.atras = [[]*3, []*3, []*3]
    #     self.cubo = [self.arriba, self.frente, self.izquierda, self.derecha, self.atras, self.abajo]
    
    def __init__(self, arriba=[[]*3, []*3, []*3], frente=[[]*3, []*3, []*3], izquierda=[[]*3, []*3, []*3], derecha=[[]*3, []*3, []*3],abajo=[[]*3, []*3, []*3],atras=[[]*3, []*3, []*3]):
        self.arriba = arriba
        self.frente = frente
        self.izquierda = izquierda
        self.derecha= derecha
        self.abajo = abajo
        self.atras = atras
        self.cubo = [self.arriba, self.frente, self.izquierda, self.derecha, self.atras, self.abajo]

    def mostrar_sector(self, lado):
        for i in range(len(lado)):
            for j in range(len(lado[i])):
                print(lado[i][j], end=" ")
            print()
        print("-----------------------")
    def __eq__(self, otro):
        if isinstance(otro, CuboRubik):
            return (self.arriba, self.frente, self.izquierda, self.derecha, self.abajo, self.atras) == (otro.arriba, otro.frente, otro.izquierda, otro.derecha, otro.abajo, otro.atras)
        return False

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

    def insertar_datos_cubo(self,txt):
        recorrido_caras = -1
        with open(txt, 'r') as f:
            lineas = f.readlines()
        
        for indice in range(len(lineas)):
            if indice % 3 == 0:
                recorrido_caras += 1
                casillas_cubo = 0
            self.cubo[recorrido_caras][casillas_cubo] = lineas[indice].split()
            casillas_cubo += 1

    def copiar_elementos(self):
        nuevo = CuboRubik()
        copia = copy.deepcopy(self.cubo)
        nuevo.cubo = copia
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
        self.frente[2],self.derecha[2],self.atras[2],self.izquierda[2] = self.izquierda[2], self.frente[2],self.derecha[2], self.atras[2]
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
        for i in range(3):
            self.arriba[2][i], self.derecha[i][0], self.abajo[0][i], self.izquierda[i][2] = \
                self.derecha[i][0], self.abajo[0][i], self.izquierda[i][2], self.arriba[2][i]
        self.frente = self.giro_antihorario(self.frente)
        
    def Back_prima(self):
        for i in range(3):
            self.arriba[0][i], self.izquierda[2-i][0], self.abajo[2][i], self.derecha[2-i][2] = \
                self.izquierda[2-i][0], self.abajo[2][i], self.derecha[2-i][2], self.arriba[0][i]
        self.atras = self.giro_antihorario(self.atras)        

    def Left_prima(self):
        columnas = self.columnas_laterales([self.arriba,self.frente,self.abajo,self.atras],2,0)
        for filas in range(3):
          self.arriba[filas][0] = columnas[3][filas]
          self.frente[filas][0] = columnas[0][filas]
          self.abajo[filas][0] = columnas[1][filas]
          self.atras[filas][2] = columnas[2][filas]
        self.izquierda = self.giro_antihorario(self.izquierda)

    def Right_prima(self):
        columnas = self.columnas_laterales([self.arriba,self.frente,self.abajo,self.atras],0,2)
        for filas in range(3):
          self.arriba[filas][2] = columnas[1][filas]
          self.frente[filas][2] = columnas[2][filas]
          self.abajo[filas][2] = columnas[3][filas]
          self.atras[filas][0] = columnas[0][filas]
        self.derecha = self.giro_antihorario(self.derecha)

    def Down_prima(self):
        self.frente[2],self.derecha[2],self.atras[2],self.izquierda[2] = self.derecha[2], self.atras[2],self.izquierda[2], self.frente[2]
        self.abajo = self.giro_antihorario(self.abajo)