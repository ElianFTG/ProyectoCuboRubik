

class CuboRubik:
    def __init__(self):
        self.arriba = [[]*3, []*3, []*3]
        self.frente = [[]*3, []*3, []*3]
        self.izquierda = [[]*3, []*3, []*3]
        self.derecha= [[]*3, []*3, []*3]
        self.abajo = [[]*3, []*3, []*3]
        self.atras = [[]*3, []*3, []*3]
        self.cubo = [self.arriba, self.frente, self.izquierda, self.derecha, self.atras, self.abajo]

    def mostrar_sector(self, lado):
        for i in range(len(lado)):
            for j in range(len(lado[i])):
                print(lado[i][j], end=" ")
            print()
     
    def __eq__(self, otro):
        if isinstance(otro, CuboRubik):
            return (self.arriba, self.frente, self.izquierda, self.derecha, self.abajo, self.atras) == (otro.arriba, otro.frente, otro.izquierda, otro.derecha, otro.abajo, otro.atras)
        return False

    def mostrar_cubo(self):
        lados = ['arriba', 'frente', 'izquierda', 'derecha', 'atrás', 'abajo']
        for indice in range(len(lados)):
            print(lados[indice])
            self.mostrar_sector(self.cubo[indice])
            print("-----------")


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

    def Up(self):
        self.izquierda[0], self.frente[0], self.derecha[0],self.atras[0] = self.frente[0],self.derecha[0],self.atras[0],self.izquierda[0]
        

    def Up_prima(self):
        self.derecha[0], self.atras[0],self.izquierda[0],self.frente[0] = self.frente[0],self.derecha[0],self.atras[0],self.izquierda[0]
        # Funciones de giro en sentido horario
    def Front(self):
        temp_up = self.arriba[-1][:]
        temp_down = self.abajo[0][:]


        for i in range(3):
            self.arriba[-1][i] = self.izquierda[i][-1]
            self.abajo[0][i] = self.derecha[i][0]
            self.izquierda[i][-1] = temp_down[i]
            self.derecha[i][0] = temp_up[i]

        self.frente = list(map(list, zip(*self.frente[::-1])))

        

    def transpuesta(self, matriz):
        repositorio = [[],[],[]]
        for fila in range(3):
            for columna in range(3):
                repositorio[fila].append(matriz[columna][fila])
        return repositorio
        
        

    def Left(self):
        for i in range(3):
            self.arriba[i][0], self.atras[2-i][2], self.abajo[i][0], self.frente[i][0] = \
                self.atras[2-i][2], self.abajo[i][0], self.frente[i][0], self.arriba[i][0]
        self.izquierda = list(map(list, zip(*self.izquierda[::-1])))
        

    def Right(self):
        for i in range(3):
            self.arriba[i][2], self.atras[2-i][0], self.abajo[i][2], self.frente[i][2] = \
                self.frente[i][2], self.arriba[i][2], self.atras[2-i][0], self.abajo[i][2]
        self.derecha = list(map(list, zip(*self.derecha[::-1])))
        

    def Back_prima(self):
        for i in range(3):
            self.arriba[0][i], self.izquierda[2-i][0], self.abajo[2][i], self.derecha[2-i][2] = \
                self.izquierda[2-i][0], self.abajo[2][i], self.derecha[2-i][2], self.arriba[0][i]
        self.atras = list(map(list, zip(*self.atras[::-1])))

        

    def Down(self):
        self.frente[2],self.derecha[2],self.atras[2],self.izquierda[2] = self.izquierda[2], self.frente[2],self.derecha[2], self.atras[2]
        

    # Funciones de giro en sentido antihorario
    def Front_prima(self):
        for i in range(3):
            self.arriba[2][i], self.derecha[i][0], self.abajo[0][i], self.izquierda[i][2] = \
                self.derecha[i][0], self.abajo[0][i], self.izquierda[i][2], self.arriba[2][i]
        self.frente = list(map(list, zip(*self.frente[::-1])))

        

    def Left_prima(self):
        for i in range(3):
            self.arriba[i][0], self.frente[i][0], self.abajo[i][0], self.atras[2-i][2] = \
                self.frente[i][0], self.abajo[i][0], self.atras[2-i][2], self.arriba[i][0]
        self.izquierda = list(map(list, zip(*self.izquierda[::-1])))

    def Right_prima(self):
        for i in range(3):
            self.arriba[i][2], self.frente[i][2], self.abajo[i][2], self.atras[2-i][0] = \
                self.atras[2-i][0], self.arriba[i][2], self.frente[i][2], self.abajo[i][2]
        self.derecha = list(map(list, zip(*self.derecha[::-1])))

    def Back(self):
        for i in range(3):
            self.arriba[0][i], self.derecha[2-i][2], self.abajo[2][i], self.izquierda[2-i][0] = \
                self.derecha[2-i][2], self.abajo[2][i], self.izquierda[2-i][0], self.arriba[0][i]
        self.atras = list(map(list, zip(*self.atras[::-1])))

    def Down_prima(self):
        self.frente[2],self.derecha[2],self.atras[2],self.izquierda[2] = self.derecha[2], self.atras[2],self.izquierda[2], self.frente[2]

    


