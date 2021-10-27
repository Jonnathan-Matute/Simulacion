# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 20:15:33 2021

@author: Jonnathan
"""

from random import randint
import matplotlib.pyplot as plot

resultado = list()
tiros = int(input("Ingrese el numero de tiros: "))
dado1 = [randint(1, 6) for p in range(1, tiros+1)]
print(dado1)
dado2 = [randint(1, 6) for p in range(1, tiros+1)]
print(dado2)
for x in range(0, len(dado1)):
    resultado.append(dado1[x]+dado2[x])
print('Resultado: ', resultado)
intervalos = range(min(resultado), max(resultado) + 2)

plot.hist(x=resultado, bins=intervalos, color='#F2AB6D', rwidth=0.85)
plot.title('Histograma')
plot.xlabel('Sumatoria')
plot.ylabel('Frecuencia')
plot.xticks(intervalos)
plot.show()
