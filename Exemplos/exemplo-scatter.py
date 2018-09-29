import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.random.randn(1000)
y = np.random.randn(1000)
ax.scatter(x,y)
plt.show()
import csv
# abre o arquivo 'arquivo.csv' em modo leitura
with open('arquivo.csv') as csvfile:
    # cria um leitor csv do arquivo
    leitor_csv = csv.reader(csvfile)
    # para cada linha deste arquivo, extrai o campo
    for row in spamreader: