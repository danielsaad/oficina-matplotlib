import matplotlib.pyplot as plt
import numpy as np
#   cria uma figura
fig = plt.figure()
#   cria um objeto axis na posição 111
ax = fig.add_subplot(111)
#   Gera de acordo com a distribuição normal de média 0 e variância 1
#   100 amostras
values = np.random.randn(10000)
#   Classifica estas 100000 amostras em 100 categorias
ax.hist(values,100,color='red')
#   Mostra o gráfico
plt.show()
