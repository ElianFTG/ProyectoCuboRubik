from Cubo_rubik import *
from BusquedasGrafos import *

def mover_piezas():
    cubo = CuboRubik() 
    cubo
    pass


matriz_generica = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

cubo = CuboRubik()
cubo.insertar_datos_cubo("lecturacubo.txt")
#cubo2.insertar_datos_cubo("lecturacubo.txt")
cubo.Down_prima()
cubo.mostrar_cubo()

