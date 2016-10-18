import matplotlib.pyplot as plt
import numpy as np
fig1 = plt.figure();
fig2 = plt.figure();
fig3 = plt.figure();
fig4 = plt.figure();
fig5 = plt.figure();

ax1 = fig1.add_subplot(111)
ax2 = fig2.add_subplot(111)
ax3 = fig3.add_subplot(111)
ax4 = fig4.add_subplot(111)
ax5 = fig5.add_subplot(111)


dom1 = np.arange(-20,20.1,0.1)
dom2 = np.arange(0.1,100,0.1)
dom3 = np.arange(0,10.5,1)
dom4 = np.arange(0,10.5,1)
dom5 = np.arange(-10,10.5,0.5)

img1 = [x**2 for x in dom1]
img2 = [np.log2(x) for x in dom2]
img3 = [np.math.factorial(x) for x in dom3]
img4 = [2**x for x in dom4]
img5 = [np.sin(x) for x in dom5]

ax1.plot(dom1,img1,color = 'gray',label=r"$f(x) = x^2$")
ax2.plot(dom2,img2,color='red',linestyle = '-.',label=r"$f(x) = \log_2(x)$")
ax3.plot(dom3,img3,color = 'green', marker='o',linestyle = ' ',label=r"$f(x) = x!$")
ax4.plot(dom4,img4,color = 'yellow',marker = 's',linestyle=' ',label=r"$f(x) = 2^x$")
ax5.plot(dom5,img5,color = 'blue',marker = '^',linestyle = '--',label=r"$f(x)=\sin(x)$")

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)
ax5.grid(True)

ax1.set_xticks(np.arange(-20,20.1,1))
ax2.set_xticks(np.arange(0.1,100,5))
ax3.set_xticks(dom3)
ax4.set_xticks(dom4)
ax5.set_xticks(dom5)

ax1.legend(loc='best')
ax2.legend(loc='best')
ax3.legend(loc='best')
ax4.legend(loc='best')
ax5.legend(loc='best')

ax1.set_title("Comportamento da Função"+r"$f(x)=x^2$")
ax2.set_title("Comportamento da Função"+r"$f(x) = \log_2(x)$")
ax3.set_title("Comportamento da Função"+r"$f(x) = x!$")
ax4.set_title("Comportamento da Função"+r"$f(x) = 2^x$")
ax5.set_title("Comportamento da Função"+r"$f(x)=\sin(x)$")

plt.show()
