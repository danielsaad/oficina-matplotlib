import matplotlib.pyplot as plt
import numpy as np
#   cria uma figura
fig = plt.figure()
#   cria um objeto axis na posição 111
ax = fig.add_subplot(111)


b2tf = [6,1,3]
matrix=[7,1,2]
jp = [7,2,1]
godfather = [5,4,1]
indiana_jones = [4,5,1]
movies = [b2tf,matrix,jp,godfather,indiana_jones]
colors=['red','green','blue','yellow','gray']
labels = ['Back to the future','Matrix','Jurassic Park','Poderoso Chefão','Indiana Jones']
width = 0.3
gap = .5
for i,movie in enumerate(movies):
    locs = [i+i*gap+x*width for x in range(len(movie))]
    ax.bar(locs,movie,width=width,color=colors[i],label=labels[i])
ax.legend(loc='best')
ax.set_yticks(np.arange(0,11,1))
ax.set_title("Preferência da Trilogia")
ax.set_xlabel("Deslocamento no eixo x")
ax.set_ylabel("Altura")
plt.show()
