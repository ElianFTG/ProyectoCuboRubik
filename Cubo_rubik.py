from colorama import Fore, Style

class CuboRubik:
    def __init__(self):
        self.cubo = [['Blanco']*9, ['Verde']*9, ['Rojo']*9, ['Azul']*9, ['Naranja']*9, ['Amarillo']*9]

    def mostrar_cubo(self):
        colores = ['Blanco', 'Verde', 'Rojo', 'Azul', 'Naranja', 'Amarillo']
        print(self.cubo[:])
        


cubo = CuboRubik()
cubo.mostrar_cubo()
