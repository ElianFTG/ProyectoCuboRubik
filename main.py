from Cubo_rubik import *
from collections import deque
import time

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

def control_redundancia(giros, giro_futuro):
    copia = giros[-3:].copy()
    copia.append(giro_futuro)
    contados = Counter(copia)
    if contados[giro_futuro] >= 3:
        return False
    return True

def bfs(cubo_raiz, cubo_solucion):
        queue = deque([(cubo_raiz, [])])
        while queue:
            estado_actual, giros = queue.popleft()
            if estado_actual == cubo_solucion:
                giros.append("terminado")
                return giros
            for giro in ["Up","Right","Left","Front","Down","Back","Up'","Right'","Left'","Front'","Back'","Down'"]:
                nuevo_estado = estado_actual.copiar_elementos()
                if(control_redundancia(giros,giro)):
                    nuevo_estado.girar_pieza(giro)
                    queue.append((nuevo_estado, giros + [giro]))
        return None

armado = cubo_armado()
while(True):
    print("Bienvenido Cubo IA, este programa sirve para la resolucion de un cubo de rubik")
    print("Inserta un cubo rubik que sea valido ya sea con su ubicacion en el equipo o el nombre siempre y cuando este este dentro de este directorio")
    url = input()
    cubo_insertado = insertar_cubo(url)
    if cubo_armado.valido:
        # inicio = time.time()
        pasos = bfs(cubo_insertado, armado)
        if pasos != None:
            print("pasos para armar")
            print(pasos)
        else:
            print("No se pudo armar el cubo")
        # fin = time.time()
        # tiempo_transcurrido = fin - inicio
        # print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos")


