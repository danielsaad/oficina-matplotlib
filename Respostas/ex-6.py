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
    fig4 = plt.figure()
    ax4 = fig4.add_subplot(111)
    fig5 = plt.figure()
    ax5 = fig5.add_subplot(111)

    nordeste = ['BAHIA','PIAUÍ','PARAÍBA','MARANHÃO','PERNAMBUCO','CEARÁ',
    'RIO GRANDE DO NORTE','ALAGOAS','SERGIPE']
    sudeste = ['MINAS GERAIS','SÃO PAULO','RIO DE JANEIRO','ESPÍRITO SANTO']
    sul = ['RIO GRANDE DO SUL','PARANÁ','SANTA CATARINA']
    centro_oeste = ['DISTRITO FEDERAL','GOIÁS','MATO GROSSO','MATO GROSSO DO SUL']
    norte = ['PARÁ','TOCANTINS','AMAZONAS','RONDÔNIA','ACRE','AMAPÁ','RORAIMA']

    data = read_csv(filename)
    pop_m_nordeste = sum([float(x[5]) for x in data[1:] if x[2] in nordeste])
    pop_f_nordeste = sum([float(x[6]) for x in data[1:] if x[2] in nordeste])
    pop_m_sudeste = sum([float(x[5]) for x in data[1:] if x[2] in sudeste])
    pop_f_sudeste = sum([float(x[6]) for x in data[1:] if x[2] in sudeste])
    pop_m_sul = sum([float(x[5]) for x in data[1:] if x[2] in sul])
    pop_f_sul = sum([float(x[6]) for x in data[1:] if x[2] in sul])
    pop_m_centro_oeste = sum([float(x[5]) for x in data[1:] if x[2] in centro_oeste])
    pop_f_centro_oeste = sum([float(x[6]) for x in data[1:] if x[2] in centro_oeste])
    pop_m_norte = sum([float(x[5]) for x in data[1:] if x[2] in norte])
    pop_f_norte = sum([float(x[6]) for x in data[1:] if x[2] in norte])


    percentual_m_nordeste = (100*(pop_m_nordeste)/(pop_m_nordeste + pop_f_nordeste))
    percentual_f_nordeste = 100 - percentual_m_nordeste
    percentual_m_sudeste = (100*(pop_m_sudeste)/(pop_m_sudeste + pop_f_sudeste))
    percentual_f_sudeste = 100 - percentual_m_sudeste
    percentual_m_sul= (100*(pop_m_sul)/(pop_m_sul+ pop_f_sul))
    percentual_f_sul= 100 - percentual_m_sul
    percentual_m_centro_oeste = (100*(pop_m_centro_oeste)/(pop_m_centro_oeste
    + pop_f_centro_oeste))
    percentual_f_centro_oeste = 100 - percentual_m_centro_oeste
    percentual_m_norte = (100*(pop_m_norte)/(pop_m_norte + pop_f_norte))
    percentual_f_norte = 100 - percentual_m_norte


    ax1.set_title("Quantidade Relativa Segundo o Sexo para a Região Nordeste")
    ax1.pie([percentual_m_nordeste,percentual_f_nordeste],
    labels=['Masculino','Feminino'],shadow=True,autopct='%1.1f%%')
    ax1.legend(loc='best')

    ax2.set_title("Quantidade Relativa Segundo o Sexo para a Região Sudeste")
    ax2.pie([percentual_m_sudeste,percentual_f_sudeste],
    labels=['Masculino','Feminino'],shadow=True,autopct='%1.1f%%')
    ax2.legend(loc='best')

    ax3.set_title("Quantidade Relativa Segundo o Sexo para a Região Sul")
    ax3.pie([percentual_m_sul,percentual_f_sul],
    labels=['Masculino','Feminino'],shadow=True,autopct='%1.1f%%')
    ax3.legend(loc='best')

    ax4.set_title("Quantidade Relativa Segundo o Sexo para a Região Centro-Oeste")
    ax4.pie([percentual_m_centro_oeste,percentual_f_centro_oeste],
    labels=['Masculino','Feminino'],shadow=True,autopct='%1.1f%%')
    ax4.legend(loc='best')

    ax5.set_title("Quantidade Relativa Segundo o Sexo para a Região Norte")
    ax5.pie([percentual_m_norte,percentual_f_norte],
    labels=['Masculino','Feminino'],shadow=True,autopct='%1.1f%%')
    ax5.legend(loc='best')
    plt.show()



if __name__ == '__main__':
    plot("../Dados/vw_razao_de_sexo.csv")
