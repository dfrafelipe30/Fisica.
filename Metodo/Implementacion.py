import numpy as np
import matplotlib.pyplot as plt

def funtionEuler(h,funcion,resultados):
    for i in range(len(resultados)):
        answers = funcion[i] + resultados[i] * h
        funcion.append(answers)
        #x[i] = x[i - 1] + h
    return  funcion 

#m = float(input("El peso del cuerpo: "))
vI= float(input("La velocidad inicial: "))
t = float(input("El angulo inicial: "))    
h = float(input("Tamano del paso: "))
N = int(input("Hasta que tamano: "))


vxo = vI * np.cos(t)
vyo = vI * np.sinc(t)
x =[]
y = []
x.append(vxo)
y.append(vyo) 


xx = [0]
xy =[0]

g = [-9.8 for i in range(N)]

c = [0 for i in range(N)]

vx = funtionEuler(h, x ,c)
vy = funtionEuler(h,y, g)

xx = funtionEuler(h, xx, vx)
xy = funtionEuler(h, xy, vy)

plt.plot(xx,xy) 
plt.show()
