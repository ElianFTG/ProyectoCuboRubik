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


cubo.Left()

# cubo2 = CuboRubik()
# cubo2 = cubo.copiar_elementos()
# cubo.Right()

#cubo.mostrar_cubo()
# print("########")
# cubo2.mostrar_cubo()

