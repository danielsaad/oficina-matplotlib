import matplotlib.pyplot as plt
import numpy as np
#   cria uma figura
fig = plt.figure()
#   cria um objeto axis na posição 111
ax = fig.add_subplot(111)


# Preferências do De Volta para o Futuro
b2tf = [5, 1, 3]
# Preferências do Matrix
matrix = [5, 1, 2]
# Preferências do Jurassic Park
jp = [5, 2, 1]
# Preferências do Poderoso Chefão
godfather = [5, 4, 1]
# Preferências do Indiana Jones
indiana_jones = [4, 1, 5]
# Preferências do Star Wars
sw = [5, 4, 5]
# Faz uma lista das preferências de cada trilogia
movies = [b2tf, matrix, jp, godfather, indiana_jones, sw]
# Especifica as cores para cada trilogia
colors = ['red', 'green', 'blue', 'yellow', 'gray', 'cyan']
# Especifica as legendas para cada trilogia
labels = ['Back to the future', 'Matrix', 'Jurassic Park',
          'Poderoso Chefão', 'Indiana Jones', 'Star Wars']
# Largura das barras
width = 0.2
# Espaço entre barras de diferentes trilogias
gap = .5
# Para cada trilogia, plota um conjunto de três barras.
for i, movie in enumerate(movies):
    locs = [i+i*gap+x*width for x in range(len(movie))]
    ax.bar(locs, movie, width=width, color=colors[i], label=labels[i])
ax.legend(loc='best')
ax.set_yticks(np.arange(0, 8, 1))
ax.set_title("Preferência da Trilogia")
ax.set_xlabel("Deslocamento no eixo x")
ax.set_ylabel("Altura")
plt.show()
