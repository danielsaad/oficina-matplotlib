"""
    Autor: Daniel Saad Nogueira Nunes
    Comentários: Exemplo da plotagem da função $f(x) = x$ utilizando
    a biblioteca Matplotlib. Neste caso são adicionadas informações nos
    eixos x e y do gráfico e a legenda correspondente. Além disso, o grid
    é inserido para melhor visualização do gráfico. Cuidadosamente, os rótulos
    dos marcadores dos eixos x e y são configurados neste exemplo.
"""

import matplotlib.pyplot as plt
import numpy as np

#   Cria um objeto figura e o coloca em fig
fig = plt.figure()
#   Da figura criada, é alocada uma matriz 1x1 de gráficos
#   ax corresponde a matriz 1
ax = fig.add_subplot(111);
#   Gera o dominio da função y = x
x  = np.arange(0,10,0.1) # domínio da função [0,10] com amostras de tamanho 0.1
#   Gera a imagem da função y = x
y = [ a for a in x ]
#   Plota a imagem e anota a legenda do gráfico
l = plt.plot(x,y,label=r"$f(x)=x$")
#   Coloca um título correspondente na figura
t = ax.set_title("Gráfico da Função"+r"$f(x) = x$")
#   Insere título no eixo x
t_x = ax.set_xlabel("Domínio da função")
#   Insere título no eixo y
t_y = ax.set_ylabel("Imagem da Função")
#   Insere  a legenda
l = ax.legend(loc='best')
#   Seta a visualização do Grid como verdadeira
ax.grid(True)
#   Seta os marcadores de 0 a 10 com espaçamento de 0.5 no eixo x
ax.set_xticks(np.arange(0,10.5,0.5))
#   Seta os marcadores de 0 a 10 com espaçamento de 0.5 no eixo y
ax.set_yticks(np.arange(0,10.5,0.5))
#   Mostra a figura fig resultante
plt.show()
