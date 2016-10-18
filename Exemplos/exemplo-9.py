"""
    Autor: Daniel Saad Nogueira Nunes
    Comentários: Exemplo de múltiplas funções sob a mesma figura.
    Manualmente escolhemos a cor e os estilos de cada função.
"""

import matplotlib.pyplot as plt
import numpy as np

#   Cria um objeto figura e o coloca em fig
fig = plt.figure()
#   Da figura criada, é alocada uma matriz 1x1 de gráficos
#   ax corresponde a matriz 1
ax = fig.add_subplot(111);

#   Gera o conjunto dominio [0,10) com amostras de tamanho 0.5
x1 = x2   = np.arange(0,10,0.5)
#   Gera a imagem da função y = sin(x)
y1 = [ np.sin(a) for a in x1 ]
#   Gera a imagem da função y = cos(x)
y2 = [ np.cos(a) for a in x2 ]

#   Plota a imagem e anota a legenda do gráfico bem como as cores e estilos
#   de linha a serem utilizados
l1 = plt.plot(x1,y1,label=r"$f(x)=\sin(x)$",color='green',linestyle='-',marker='o')
l2 = plt.plot(x2,y2,label=r"$g(x)=\cos(x)$",color='blue',linestyle='--',marker='s')
#   Coloca um título correspondente na figura
t = ax.set_title("Comportamento das funções seno e cosseno")
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
ax.set_yticks(np.arange(-2,2.5,0.5))
#   Mostra a figura fig resultante
plt.show()
