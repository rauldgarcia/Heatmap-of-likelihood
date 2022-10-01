import pandas as pd
import numpy as np
import seaborn as sns
import random
import matplotlib.pyplot as plt
import math

#calculo de likelihood
def ml (mu,sigma,xi):
    for i in range(10):
        suma=((xi[i]-mu)**2)/(sigma**2)
        
    expo=math.exp(-0.5*suma)
    aux=1/((2*math.pi*(sigma**2))**5)
    return aux*expo

def normal (x,mu,sigma):
    return np.exp(-1*((x-mu)**2)/(2*(sigma**2)))/(math.sqrt(2*np.pi) * sigma)

# VALORES DADOS
mux=5
sigmax=1.5
mu1=3
sigma1=1
mu2=6
sigma2=1.6
mu3=5.1
sigma3=1.4

nums=np.array([])
ynums=np.array([])
auxi=0
auxi2=0
sigmap=0

#CREACION DE PUNTOS ALEATORIOS BASADO EN DATOS DE GAUSSIANA
for i in range(10):
    x=random.gauss(mux, sigmax)
    nums=np.append(nums,x)
    ynums=np.append(ynums,0)
    auxi=auxi+x
mup=auxi/10

for i in range(10):
    auxi2=((nums[i]-mup)**2)/10
    sigmap=sigmap+auxi2

sigmap=sigmap**0.5
mlf=ml(mup,sigmap,nums)

#CREACION DE 3 GAUSSIANAS
plt.subplot(2,2,1)
li1=ml(mu1,sigma1,nums)
plt.scatter(nums,ynums,color='k')
plt.title('μ=3 σ=1')
plt.xlim(0,10)
plt.ylim(0,0.40)
x1=np.linspace(mu1-6*sigma1,mu1+6*sigma1,100)
y1=normal(x1,mu1,sigma1)
plt.plot(x1,y1,'b')
plt.legend(['Likelihood:',li1])
for i in range (10):
    plt.arrow(nums[i],ynums[i], 0,normal(nums[i],mu1,sigma1),color='b')

plt.subplot(2,2,2)
li2=ml(mu2,sigma2,nums)
plt.scatter(nums,ynums,color='k')  
plt.title('μ=6 σ=1.6')
plt.xlim(0,10)
plt.ylim(0,0.40)
x2=np.linspace(mu2-6*sigma2,mu2+6*sigma2,100)
y2=normal(x2,mu2,sigma2)
plt.plot(x2,y2,'r')
plt.legend(['Likelihood:',li2])
for i in range (10):
    plt.arrow(nums[i],ynums[i], 0,normal(nums[i],mu2,sigma2),color='r')

plt.subplot(2,2,3)
li3=ml(mu3,sigma3,nums)
plt.scatter(nums,ynums,color='k') 
plt.title('μ=5.1 σ=1.4') 
plt.xlim(0,10)
plt.ylim(0,0.40)
x3=np.linspace(mu3-6*sigma3,mu3+6*sigma3,100)
y3=normal(x3,mu3,sigma3)
plt.plot(x3,y3,'g')
plt.legend(['Likelihood:',li3])
for i in range (10):
    plt.arrow(nums[i],ynums[i], 0,normal(nums[i],mu3,sigma3),color='g')

#CREACION DE MAPA DE CALOR DE LIKELIHOOD
mus=np.array([])
for i in range(25,66,2):
    mus=np.append(mus,i/10)

sigmas=np.array([])
for i in range(0,21,1):
    sigmas=np.append(sigmas,i/10)

mls=np.zeros((20,20))
for i in range(1,20,1):
    for j in range(1,20,1):
        mls[i][j]=ml(mus[i],sigmas[j],nums)

plt.subplot(2,2,4)
sns.heatmap(mls,vmin=0,vmax=0.001,xticklabels=False,yticklabels=False)
plt.scatter((mux-2.5)*5,sigmax*10,color='blue')
plt.scatter((mup-2.5)*5,sigmap*10,color='green')
mu=str('μ=')
muc=repr(round(mup,2))
sigc=repr(round(sigmap,2))
sig=str('σ=')
pt=mu+muc+sig+sigc
plt.legend(['μ=5 σ=1.5',pt])
plt.xlim(1,20)
plt.ylim(1,20)
plt.title('LIKELIHOOD')
plt.show()