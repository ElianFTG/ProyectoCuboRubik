from Cubo_rubik import *
from collections import deque

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
print(cubo_insertado==armado)

# pasos = bfs(cubo_insertado, armado)
# if pasos != None:
#     print("pasos para armar")
#     print(pasos)
# else:
#     print("No se pudo armar el cubo")

