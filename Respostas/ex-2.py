import csv
import matplotlib.pyplot as plt

def read_csv(filename):
    with open(filename,'r') as f:
        data = list(csv.reader(f))
    return data


def plot(filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    data = read_csv(filename)
    thread_n = [col[0] for col in data[2:]]
    speedup = [col[1] for col in data[2:]]
    linear_speedup  = [col[2] for col in data[2:]]
    ax.set_xlim(0,25)
    ax.set_ylim(0,25)
    ax.set_xticks([k for k in range(1,25)])
    ax.set_yticks([k for k in range (1,25)])
    ax.plot(thread_n,linear_speedup,marker='o',color='green',label='Speedup Linear')
    ax.plot(thread_n,speedup,marker='^',color='red',label = 'Speedup')
    ax.set_title("Curva de Speedup")
    ax.set_xlabel(data[1][0])
    ax.set_ylabel(data[0][1])
    ax.legend(loc='best')
    plt.show()



if __name__ == '__main__':
    plot("../Dados/speedup.csv")
