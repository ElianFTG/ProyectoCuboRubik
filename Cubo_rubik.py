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
        lados = [, '', 'izquierda', 'derecha', 'atrás', 'abajo']
        print('arriba')
        self.mostrar_sector(self.arriba)
        print('frente')
        self.mostrar_sector(self.frente)

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
        return [list(reversed(col)) for col in zip(*matrix)]


    def Up(self):
        self.izquierda[0], self.frente[0], self.derecha[0],self.atras[0] = self.frente[0],self.derecha[0],self.atras[0],self.izquierda[0]
        self.arriba = self.giro_horario(self.arriba)
        

    def Up_prima(self):
        self.derecha[0], self.atras[0],self.izquierda[0],self.frente[0] = self.frente[0],self.derecha[0],self.atras[0],self.izquierda[0]
        self.arriba = self.giro_antihorario(self.arriba)      

    def Front(self):
        
        fila_adyacente_superior = self.arriba[2]
        fila_adyacente_abajo = self.abajo[0]
        columna_adyacente_derecha = [self.derecha[2][0],self.derecha[1][0],self.derecha[0][0]]
        columna_adyacente_izquierda = [self.izquierda[2][2],self.izquierda[1][2],self.izquierda[0][2] ]
        print(self.arriba[2])
        self.arriba[2] = columna_adyacente_izquierda
        print(self.arriba[2])
        self.derecha[0][0],self.derecha[1][0],self.derecha[2][0] = fila_adyacente_superior[0],fila_adyacente_superior[1],fila_adyacente_superior[2]
        self.izquierda[0][2],self.izquierda[1][2],self.izquierda[2][2] = fila_adyacente_abajo[0],fila_adyacente_abajo[1],fila_adyacente_abajo[2]
        self.abajo[0] = columna_adyacente_derecha

        self.frente = self.giro_horario(self.frente)
        print(self.cubo[0], " = ", self.arriba)
        
        

    def Left(self):
        for i in range(3):
            self.arriba[i][0], self.atras[2-i][2], self.abajo[i][0], self.frente[i][0] = \
                self.atras[2-i][2], self.abajo[i][0], self.frente[i][0], self.arriba[i][0]


    def Right(self):
        for i in range(3):
            self.arriba[i][2], self.atras[2-i][0], self.abajo[i][2], self.frente[i][2] = \
                self.frente[i][2], self.arriba[i][2], self.atras[2-i][0], self.abajo[i][2]
        
        

    def Back_prima(self):
        for i in range(3):
            self.arriba[0][i], self.izquierda[2-i][0], self.abajo[2][i], self.derecha[2-i][2] = \
                self.izquierda[2-i][0], self.abajo[2][i], self.derecha[2-i][2], self.arriba[0][i]
        

        

    def Down(self):
        self.frente[2],self.derecha[2],self.atras[2],self.izquierda[2] = self.izquierda[2], self.frente[2],self.derecha[2], self.atras[2]
        

    # Funciones de giro en sentido antihorario
    def Front_prima(self):
        for i in range(3):
            self.arriba[2][i], self.derecha[i][0], self.abajo[0][i], self.izquierda[i][2] = \
                self.derecha[i][0], self.abajo[0][i], self.izquierda[i][2], self.arriba[2][i]
        

        

    def Left_prima(self):
        for i in range(3):
            self.arriba[i][0], self.frente[i][0], self.abajo[i][0], self.atras[2-i][2] = \
                self.frente[i][0], self.abajo[i][0], self.atras[2-i][2], self.arriba[i][0]
        

    def Right_prima(self):
        for i in range(3):
            self.arriba[i][2], self.frente[i][2], self.abajo[i][2], self.atras[2-i][0] = \
                self.atras[2-i][0], self.arriba[i][2], self.frente[i][2], self.abajo[i][2]
        

    def Back(self):
        for i in range(3):
            self.arriba[0][i], self.derecha[2-i][2], self.abajo[2][i], self.izquierda[2-i][0] = \
                self.derecha[2-i][2], self.abajo[2][i], self.izquierda[2-i][0], self.arriba[0][i]
        

    def Down_prima(self):
        self.frente[2],self.derecha[2],self.atras[2],self.izquierda[2] = self.derecha[2], self.atras[2],self.izquierda[2], self.frente[2]
