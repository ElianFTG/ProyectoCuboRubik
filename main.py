from Cubo_rubik import *
from collections import deque
import numpy as np

def insertar_cubo(txt):
    cubo = CuboRubik()
    cubo.insertar_datos_cubo(txt)
    return cubo

def cubo_armado():
    colores = ["blanco","verde","naranja","rojo","azul","amarillo"]
    lista = np.array([np.zeros((3, 3),dtype=object)]*6)
    for cara in range(len(lista)):
        lista[cara] = [[colores[cara]]*3]*3 
    armado = CuboRubik(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5])
    return armado


def bfs(cubo_raiz, cubo_solucion):
        queue = deque([(cubo_raiz, [])])
        if cubo_raiz.valido:  
            while queue:
                estado_actual, giros = queue.popleft()
                if cubo_raiz == cubo_solucion:
                    giros.append("terminado")
                    return giros
                for giro in ["Up","Right","Left","Front","Down","Back","Up'","Right'","Left'","Front'","Back'","Down'"]:
                    nuevo_estado = estado_actual.copiar_elementos()
                    nuevo_estado.girar_pieza(giro)
                    queue.append((nuevo_estado, giros + [giro]))
            return None



# Crear un array de numpy con una dimensión mínima


# armado = CuboRubik(np.array([[["blanco"]*3]*3],dtype=object),
#                    np.array([[["verde"]*3]*3],dtype=object),
#                    np.array([[["naranja"]*3]*3],dtype=object),
#                    np.array([[["rojo"]*3]*3],dtype=object),
#                    np.array([[["azul"]*3]*3],dtype=object),
#                    np.array([[["amarillo"]*3]*3],dtype=object))
# armado.cubo = np.array([[["blanco"]*3]*3,
#                         [["verde"]*3]*3,
#                         [["naranja"]*3]*3,
#                         [["rojo"]*3]*3,
#                         [["azul"]*3]*3,
#                         [["amarillo"]*3]*3],dtype=object)
# armado.mostrar_cubo()
url = input()
cubo_insertado = insertar_cubo(url)
armado = cubo_armado()
#print(cubo_insertado)
# cubo_insertado.Left()

# cubo_insertado.Front()

# cubo_insertado.Down_prima()


# cubo_insertado.Back()

# cubo_insertado.Left_prima()
# cubo_insertado.Down()
armado.mostrar_cubo()


pasos = bfs(cubo_insertado, armado)
if pasos != None:
    print("pasos para armar")
    print(pasos)
else:
    print("No se pudo armar el cubo")

# mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# mat2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(len(mat1)) 
# print(np.array_equal(mat1,mat2))