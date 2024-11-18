import numpy as np
import matplotlib.pyplot as plt

languages = np.genfromtxt("/home/diegobm23/projetos-diegobm23/diego-scripts/Popular-Programming-Languages-2004-2022.csv", delimiter=",", skip_header=1, dtype='S')
size = 48


def show_graf(x, y, title):
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r')
    ax.set(title=title)
    ax.grid()
    plt.show()


def compare_java():
    x = languages[-size:, :1].reshape(size).astype(int)
    y = languages[-size:, 12:13].reshape(size).astype(float)
    show_graf(x, y, "Popularidade do Java nos últimos 4 anos")


def compare_javascript():
    x = languages[-size:, :1].reshape(size).astype(int)
    y = languages[-size:, 13:14].reshape(size).astype(float)
    show_graf(x, y, "Popularidade do Javascript nos últimos 4 anos")


def compare_python():
    x = languages[-size:, :1].reshape(size).astype(int)
    y = languages[-size:, 21:22].reshape(size).astype(float)
    show_graf(x, y, "Popularidade do Python nos últimos 4 anos")


compare_java()
compare_javascript()
compare_python()
