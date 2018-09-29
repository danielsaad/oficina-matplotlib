import csv

# Valores iniciais da sequência de Fibonacci
f1 = 1
f2 = 1
# abre um arquivo no modo de escrita

with open('fib.csv', 'w') as csvfile:
    # cria um escritor csv do arquivo
    escritor_csv = csv.writer(csvfile, delimiter=',')
    # Escreve o cabeçalho
    escritor_csv.writerow(['Índice', 'Número de Fibonacci', 'Razão de Ouro'])
    # Escreve os dois primeiros números de Fibonacci e a razão entre eles
    escritor_csv.writerow(['1', str(f1),''])
    escritor_csv.writerow(['2', str(f2),'1'])
    # Faça 1000 iterações e preencha os números de Fibonacci no arquivo csv
    for i in range(3,1000):
        # Escreve em uma string o índice, o próximo número de fibonacci e a razão de ouro calculada
        string = "{} {} {}".format(i,f1+f2,(f1+f2)/float(f2))
        # Transforma a string em uma lista
        linha = string.split(' ')
        # Escreve a linha no arquivo csv
        escritor_csv.writerow(linha)
        # Calcula o próximo número de Fibonacci
        temp = f1
        f1 = f2
        f2 = temp +f2