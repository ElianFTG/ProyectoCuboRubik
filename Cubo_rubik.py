

class CuboRubik:
    def __init__(self):
        self.arriba = [[]*3, []*3, []*3]
        self.frente = [[]*3, []*3, []*3]
        self.izquierda = [[]*3, []*3, []*3]
        self.derecha= [[]*3, []*3, []*3]
        self.abajo = [[]*3, []*3, []*3]
        self.atras = [[]*3, []*3, []*3]
        self.cubo = [self.arriba, self.frente, self.izquierda, self.derecha, self.abajo, self.atras]

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
        lados = ['arriba', 'frente', 'izquierda', 'derecha', 'abajo', 'atrás']
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

    def girar_cara_horario(self, cara):
        cara[:] = [list(reversed(col)) for col in zip(*cara)]

    def girar_cara_antihorario(self, cara):
        cara[:] = [list(col[::-1]) for col in zip(*cara)]
    
    def girar_arriba_horario(self):
        self.girar_cara_horario(self.arriba)
        temp = [self.frente[0][:], self.izquierda[0][:], self.atras[0][:], self.derecha[0][:]]
        self.frente[0], self.izquierda[0], self.atras[0], self.derecha[0] = temp[1], temp[2], temp[3], temp[0]

    def girar_arriba_antihorario(self):
        self.girar_cara_antihorario(self.arriba)
        temp = [self.frente[0][:], self.izquierda[0][:], self.atras[0][:], self.derecha[0][:]]
        self.frente[0], self.izquierda[0], self.atras[0], self.derecha[0] = temp[3], temp[0], temp[1], temp[2]

    def girar_frente_horario(self):
        self.girar_cara_horario(self.frente)
        temp = [self.arriba[2][:], list(reversed(self.izquierda[2])), self.abajo[0][:], list(reversed(self.derecha[0]))]
        self.arriba[2], self.izquierda[2], self.abajo[0], self.derecha[0] = temp[1], temp[2], temp[3], temp[0]

    def girar_frente_antihorario(self):
        self.girar_cara_antihorario(self.frente)
        temp = [self.arriba[2][:], list(reversed(self.izquierda[2])), self.abajo[0][:], list(reversed(self.derecha[0]))]
        self.arriba[2], self.izquierda[2], self.abajo[0], self.derecha[0] = temp[3], temp[0], temp[1], temp[2]

    def girar_izquierda_horario(self):
        self.girar_cara_horario(self.izquierda)
        temp = [self.arriba[:][0], self.atras[::-1][0], self.abajo[:][0], self.frente[:][0]]
        self.arriba[:][0], self.atras[::-1][0], self.abajo[:][0], self.frente[:][0] = temp[1], temp[2], temp[3], temp[0]

    def girar_izquierda_antihorario(self):
        self.girar_cara_antihorario(self.izquierda)
        temp = [self.arriba[:][0], self.atras[::-1][0], self.abajo[:][0], self.frente[:][0]]
        self.arriba[:][0], self.atras[::-1][0], self.abajo[:][0], self.frente[:][0] = temp[3], temp[0], temp[1], temp[2]

    def girar_derecha_horario(self):
        self.girar_cara_horario(self.derecha)
        temp = [self.arriba[:][2], self.frente[:][2], self.abajo[:][2], self.atras[::-1][2]]
        self.arriba[:][2], self.frente[:][2], self.abajo[:][2], self.atras[::-1][2] = temp[3], temp[0], temp[1], temp[2]

    def girar_derecha_antihorario(self):
        self.girar_cara_antihorario(self.derecha)
        temp = [self.arriba[:][2], self.frente[:][2], self.abajo[:][2], self.atras[::-1][2]]
        self.arriba[:][2], self.frente[:][2], self.abajo[:][2], self.atras[::-1][2] = temp[1], temp[2], temp[3], temp[0]

    def girar_abajo_horario(self):
        self.girar_cara_horario(self.abajo)
        temp = [self.frente[2][:], self.derecha[2][:], self.atras[2][:], self.izquierda[2][:]]
        self.frente[2], self.derecha[2], self.atras[2], self.izquierda[2] = temp[1], temp[2], temp[3], temp[0]

    def girar_abajo_antihorario(self):
        self.girar_cara_antihorario(self.abajo)
        temp = [self.frente[2][:], self.derecha[2][:], self.atras[2][:], self.izquierda[2][:]]
        self.frente[2], self.derecha[2], self.atras[2], self.izquierda[2] = temp[3], temp[0], temp[1], temp[2]

    def girar_atras_horario(self):
        self.girar_cara_horario(self.atras)
        temp = [self.arriba[::-1][2], self.derecha[::-1][2], self.abajo[::-1][2], self.izquierda[::-1][2]]
        self.arriba[::-1][2], self.derecha[::-1][2], self.abajo[::-1][2], self.izquierda[::-1][2] = temp[3]
        


