"""
    Autor: Daniel Saad Nogueira Nunes
    Comentários: Exemplo minimalista da plotagem da função f(x) = x utilizando
    a biblioteca Matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np

#   cria um objeto figura e o coloca em fig
fig = plt.figure()
#   da figura criada, é alocada uma matriz 1x1 de gráficos
#   ax corresponde a matriz 1
ax = fig.add_subplot(111)
#   gera o dominio da função y = x
#   domínio da função [0,10) com amostras de tamanho 0.1
x  = np.arange(0,10,0.1)
#   Gera a imagem da função y = x
y = np.array([ a for a in x ])
#   Plota a imagem
l = plt.plot(x,y)
#   Coloca um título correspondente na figura
t = ax.set_title("Gráfico da Função " r"$f(x) = x$")
#   Mostra o resultado na tela
plt.show()
