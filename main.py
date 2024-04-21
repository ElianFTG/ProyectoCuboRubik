from Cubo_rubik import *
from collections import deque
import numpy as np

def insertar_cubo(txt):
    cubo = CuboRubik()
    cubo.insertar_datos_cubo(txt)
    return cubo


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
                    queue.append((nuevo_estado, giros.append(giro)))
            return None


armado = CuboRubik()
armado.cubo = [["blanco"]*9,["verde"]*9,["naranja"]*9,["rojo"]*9,["azul"]*9,["amarillo"]*9]
url = input()
cubo_insertado = insertar_cubo(url)

cubo_insertado.Left()

cubo_insertado.Front()

cubo_insertado.Down_prima()


cubo_insertado.Back()

cubo_insertado.Left_prima()
cubo_insertado.Down()
cubo_insertado.mostrar_cubo()
# print(cubo_insertado==armado)

# pasos = bfs(cubo_insertado, armado)
# if pasos != None:
#     print("pasos para armar")
#     print(pasos)
# else:
#     print("No se pudo armar el cubo")

# mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# mat2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(len(mat1)) 
# print(np.array_equal(mat1,mat2))