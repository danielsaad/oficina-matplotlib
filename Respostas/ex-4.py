import csv
import matplotlib.pyplot as plt
import numpy as np
def read_csv(filename):
    with open(filename,'r') as f:
        data = list(csv.reader(f))
    return data


def plot(filename):
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)

    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111)


    data = read_csv(filename)
    notas_p1 = [float(col[1]) for col in data[1:]]
    medias = [(float(col[1]) + float(col[2]) + float(col[3]))/3.0 for col in data[1::]]
    aprovados = [x for x in medias if x>=6.0]
    reprovados = [x for x in medias if x<6.0]
    bins = range(0,11,1)
    ax1.hist(notas_p1,bins=bins,color='red',label='Histograma da Prova 1')
    ax1.set_xticks(range(0,11,1))

    ax2.bar(0,len(aprovados),width=0.1,color='red',label='Reprovados')
    ax2.bar(0.2,len(reprovados),width=0.1,color='blue',label='Aprovados')
    ax2.set_ylim(0,len(aprovados)+len(reprovados))

    print(aprovados)
    print(reprovados)
    ax3.pie([len(aprovados),len(reprovados)],labels=['Aprovados','Reprovados'],
        colors=['red','blue'],shadow=True,autopct='%1.1f%%')

    ax1.legend(loc='best')
    ax2.legend(loc='best')
    ax3.legend(loc='best')

    plt.show()



if __name__ == '__main__':
    plot("../Dados/notas.csv")
