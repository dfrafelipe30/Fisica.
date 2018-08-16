import numpy as np
import matplotlib.pyplot as plt

def funtionEuler(h,N,funcion,resultados):
    print funcion[0]
    for i in range(0,N):
        answers = funcion[i] + resultados[i] * h
        funcion.append(answers)
        #x[i] = x[i - 1] + h
    return  y 

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


xx = []
xy =[]

g = [-9.8 for i in np.arange(1,N)]
print g
c = [0 for i in np.arange(1,N)]

vx = funtionEuler(h, N, x , g)
vy = funtionEuler(h, N,y, c)

xx = funtionEuler(h, N, xx, vx)
xy = funtionEuler(h, N, xy, vy)

plt.scatter(xx,xy) 
plt.show()