import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

labels = ['Comédia','Ação','Romance','Drama','Ficção Científica','Terror']
colors = ['yellow','red','blue','green','purple','gray']
valores = [4,5,6,1,4,2]
width=.5
gap = 1;
locs = [np.arange(0,len(valores)*width,width)]
for i,valor in enumerate(valores):
    loc = i*width
    ax1.bar(loc,valor,width=width,color=colors[i],label=labels[i])
ax2.pie(valores,labels=labels,shadow=True,autopct='%1.1f%%',colors=colors)

ax1.set_title("Quantidade Absoluta de Respostas")
ax1.legend(loc='best')
ax2.set_title("Quantidade Relativa de Respostas")

plt.show()
