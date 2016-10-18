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

    nordeste = ['BAHIA','PIAUÍ','PARAÍBA','MARANHÃO','PERNAMBUCO','CEARÁ',
    'RIO GRANDE DO NORTE','ALAGOAS','SERGIPE']
    sudeste = ['MINAS GERAIS','SÃO PAULO','RIO DE JANEIRO','ESPÍRITO SANTO']
    sul = ['RIO GRANDE DO SUL','PARANÁ','SANTA CATARINA']
    centro_oeste = ['DISTRITO FEDERAL','GOIÁS','MATO GROSSO','MATO GROSSO DO SUL']
    norte = ['PARÁ','TOCANTINS','AMAZONAS','RONDÔNIA','ACRE','AMAPÁ','RORAIMA']

    data = read_csv(filename)
    pib_nordeste = sum([float(x[5]) for x in data[1:] if x[2] in nordeste])
    pib_sudeste = sum([float(x[5]) for x in data[1:] if x[2] in sudeste])
    pib_sul = sum([float(x[5]) for x in data[1:] if x[2] in sul])
    pib_centro_oeste = sum([float(x[5]) for x in data[1:] if x[2] in centro_oeste])
    pib_norte = sum([float(x[5]) for x in data[1:] if x[2] in norte])

    valores = [pib_nordeste,pib_sudeste,pib_sul,pib_centro_oeste,pib_norte]
    labels = ['Nordeste','Sudeste','Sul','Centro-Oeste','Norte']

    ax1.pie(valores,labels=labels,shadow=True,autopct='%1.1f%%')
    ax1.set_title("Proporção do PIB por unidade Federativa")
    plt.show()



if __name__ == '__main__':
    plot("../Dados/vw_pib_percapita.csv")
