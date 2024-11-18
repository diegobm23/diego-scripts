import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 15)


def exibirGrafico(x, y, title):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(title=title)
    ax.grid()
    plt.show()


def progrecaoaritimetica():
    y = (4 + x)
    exibirGrafico(x, y, 'Função de progressão aritmética')


def progrecaoexponencial():
    y = (x ** 2)
    exibirGrafico(x, y, 'Função de progressão exponencial')


def seno():
    y = np.sin(x)
    exibirGrafico(x, y, 'Função seno')


def cosseno():
    y = np.cos(x)
    exibirGrafico(x, y, 'Função cosseno')


def logaritmica():
    y = np.log(x)
    exibirGrafico(x, y, 'Função logarítmica')


progrecaoaritimetica()
progrecaoexponencial()
seno()
cosseno()
logaritmica()
