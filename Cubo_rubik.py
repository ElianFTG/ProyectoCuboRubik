

class CuboRubik:
    def __init__(self):
        self.arriba = [[]*3, []*3, []*3]
        self.frente = [[]*3, []*3, []*3]
        self.izquierda = [[]*3, []*3, []*3]
        self.derecha= [[]*3, []*3, []*3]
        self.abajo = [[]*3, []*3, []*3]
        self.atrás = [[]*3, []*3, []*3]
        self.cubo = [self.arriba, self.frente, self.izquierda, self.derecha, self.abajo, self.atrás]

    def mostrar_sector(self, lado):
        for i in range(len(lado)):
            for j in range(len(lado[i])):
                print(lado[i][j], end=" ")
            print()
            

    def mostrar_cubo(self):
        lados = ['arriba', 'frente', 'izquierda', 'derecha', 'abajo', 'atrás']
        for indice in range(len(lados)):
            print(lados[indice])
            self.mostrar_sector(self.cubo[indice])

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


        pass 
        


cubo = CuboRubik()
cubo.mostrar_cubo()
cubo.insertar_datos_cubo("lecturacubo.txt")
cubo.mostrar_cubo()

