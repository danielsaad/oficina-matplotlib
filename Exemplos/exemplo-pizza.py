import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
porcentagem = [9.2, 36.1, 30.3, 20.3, 3.2, 0.2, 0.7]
labels = ['Ameríndios', 'Brancos', 'Mestiços',
          'Mulatos', 'Negros', 'Zambos', 'Asiáticos']
explode = [0, 0.2, 0, 0, 0, 0, 0]
ax.set_title("Distribuição Étnica na América Latina em 2005", y=1.06)
ax.pie(porcentagem, labels=labels, explode=explode, shadow=True,
       autopct='%1.1f%%')
plt.show()
