import math 
class Particle:
    def __init__(self,posicion,velocidad):
        self.pos = posicion
        self.vel = velocidad
        
    def move(self,tiempo):
        self.pos = suma(self.pos,mul(self.vel,tiempo))
        
    def times(self,particulas,Lx,Ly,sigma):
        colisiones=[]
        colisionesparedes=[]
        for i in range(len(particulas)):
            for j in range(i,len(particulas)):
                rij=suma(particulas[i].pos,mul(particulas[j].pos,-1))
                vij=suma(particulas[i].vel,mul(particulas[j].vel,-1))
                a=-2*dot(rij,vij)
                b=(2*dot(rij,vij))**2
                c=4*(dot(vij,vij)*(dot(rij,rij)-sigma**2))
                d=2*dot(vij,vij)
                if d!=0 and b-c>=0:
                    tij=(a-math.sqrt(b-c))/d
                    if tij>0:
                        colisiones.append([tij,particulas[i],particulas[j]])
            if particulas[i].vel[0]!=0:
                colisionesparedes.append([(Lx-sigma/2-particulas[i].pos[0])/particulas[i].vel[0],particulas[i],"murox"])
            if particulas[i].vel[1]!=0:
                colisionesparedes.append([(Ly-sigma/2-particulas[i].pos[1])/particulas[i].vel[1],particulas[i],"muroy"])
            if particulas[i].vel[0]!=0:
                colisionesparedes.append([(sigma/2-particulas[i].pos[0])/particulas[i].vel[0],particulas[i],"murox"])
            if particulas[i].vel[1]!=0:
                colisionesparedes.append([(sigma/2-particulas[i].pos[1])/particulas[i].vel[1],particulas[i],"muroy"])
        return colisiones+colisionesparedes

    def changemomentum(self,p1,p2):
        if p2=="murox":
            p1.vel[0]=-p1.vel[0]
        elif p2=="muroy":
            p1.vel[1]=-p1.vel[1]
        else:
            rij=suma(p1.pos,mul(p2.pos,-1))
            sombrai=dot(p1.vel,rij)/norma(rij)
            sombraj=dot(p2.vel,rij)/norma(rij)
            rhat=mul(rij,1/norma(rij))
            p1.vel=suma(p1.vel,mul(rhat,-sombrai+sombraj))
            p2.vel=suma(p2.vel,mul(rhat,-sombraj+sombrai))     

def dot(a,b):
    s=0
    for i in range(len(a)):
        s+=a[i]*b[i]
    return s

def suma(a,b):
    s=[]
    for i in range(len(a)):
        s.append(a[i]+b[i])
    return s

def mul(a,k):
    m=[]
    for i in range(len(a)):
        m.append(k*a[i])
    return m

def norma(a):
    return math.sqrt(dot(a,a))

a=Particle([5,2],[1,0])
b=Particle([3,2],[0,0])
c=Particle([10,7],[-1,0])
d=Particle([5,7],[1,0])
p=[a,b]
historial=range(len(p))
for i in range(len(p)):
    historial[i]=[]
for i in range(4):
    for j in range(len(p)):
        print "r",p[j].pos,"v",p[j].vel
        historial[j].append(p[j].pos)
    print "-"*20
    colis=a.times(p,10,10,2)
    "print colis"
    for j in colis:
        if j[0]>0:
            mini=j[0]
            p1=j[1]
            p2=j[2]
            break
    for j in colis:
        if j[0]<mini and j[0]>0:
            mini=j[0]
            p1=j[1]
            p2=j[2]
    print "mini",mini
    for j in p:
        j.move(mini)
    a.changemomentum(p1,p2)
for i in historial:
    print i

     
    
        


