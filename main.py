from Cubo_rubik import *
from BusquedasGrafos import *
from grafo_cubo import *

def mover_piezas():
    cubo = CuboRubik() 
    cubo
    pass


matriz_generica = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print()

#matriz_generica2 = matriz_generica[:][:]
cubo = CuboRubik()
cubo.insertar_datos_cubo("lecturacubo.txt")
# cubo2 = CuboRubik(cubo.arriba[:][:],
#         cubo.frente[:][:],
#         cubo.izquierda[:][:],
#         cubo.derecha[:][:],
#         cubo.abajo[:][:],
#         cubo.atras[:][:]
#        )

#print(cubo.validacion_centros())
print(cubo.validacion_colores()[0][0])
# cubo.Left()
# cubo.Up()
# cubo.Right()
# cubo.Back()
# cubo.Front()
# cubo.Up_prima()
# cubo.Down_prima()
# cubo.Back_prima()
# cubo.Front_prima()
# cubo.Left_prima()
# cubo.Right_prima()
# print("########")


