import csv
# abre o arquivo 'arquivo.csv' em modo leitura

nome = []
time = []
idade = []
with open('arquivo.csv') as csvfile:
    # cria um leitor csv do arquivo
    leitor_csv = csv.reader(csvfile,delimiter=',')
    # ignora o cabeçalho
    next(leitor_csv,None)
    # para cada linha deste arquivo, extrai o campo
    for linha in leitor_csv:
        nome.append(linha[0])
        time.append(linha[1])
        idade.append(linha[2])


print("Imprimindo os dados")
for i in range(len(nome)):
    print("Nome = ",nome[i],"Time = ",time[i],"Idade = ",idade[i])