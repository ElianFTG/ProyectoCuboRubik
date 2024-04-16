from Cubo_rubik import *
from BusquedasGrafos import *




cubo = CuboRubik()
cubo2 = CuboRubik()
cubo.insertar_datos_cubo("lecturacubo.txt")
cubo2.insertar_datos_cubo("lecturacubo.txt")
print(cubo == cubo2)

