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
ax1 = fig.add_subplot(211);
ax2 = fig.add_subplot(212)
#   Gera o conjunto dominio [0,10) com amostras de tamanho 0.5
x1 = x2   = np.arange(0,10,0.5)
#   Gera a imagem da função f(x) = sin(x)
y1 = [ np.sin(a) for a in x1 ]
#   Gera a imagem da função g(x) = cos(x)
y2 = [ np.cos(a) for a in x2 ]

#   Plota a imagem e anota a legenda do gráfico bem como as cores e estilos
#   de linha a serem utilizados
l1 = ax1.plot(x1,y1,label=r"$f(x)=\sin(x)$",color='green',linestyle='-',marker='o')
l2 = ax2.plot(x2,y2,label=r"$g(x)=\cos(x)$",color='blue',linestyle='--',marker='s')
#   Coloca um título correspondente na figura
t1 = ax1.set_title("Comportamento da função seno")
t2 = ax2.set_title("Comportamento da função cosseno")

t_x1 = ax1.set_xlabel("Domínio da função")
#   Insere título no eixo y
t_y1 = ax1.set_ylabel("Imagem da Função")

t_x2 = ax2.set_xlabel("Domínio da função")
#   Insere título no eixo y
t_y2 = ax2.set_ylabel("Imagem da Função")
#   Insere  a legenda
l1 = ax1.legend(loc='best')
l2 = ax2.legend(loc='best')
#   Seta a visualização do Grid como verdadeira
ax1.grid(True)
ax2.grid(True);
#   Seta os marcadores de 0 a 10 com espaçamento de 0.5 no eixo x
ax1.set_xticks(np.arange(0,10.5,0.5))
ax2.set_xticks(np.arange(0,10.5,0.5))
#   Seta os marcadores de 0 a 10 com espaçamento de 0.5 no eixo y
ax1.set_yticks(np.arange(-2,2.5,0.5))
ax2.set_yticks(np.arange(-2,2.5,0.5))
#   Mostra a figura fig resultante
fig.show()
fig.savefig('seno_cosseno.png',dpi=600)
fig.savefig('seno_cosseno.pdf')
fig.savefig('seno_cosseno.svg')
