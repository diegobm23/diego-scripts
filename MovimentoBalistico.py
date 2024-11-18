# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

velocidade = float(input("Digite a velocidade em m/s: "))
angulo = float(input("Digite o ângulo de lançamento em graus: "))

ang_rad = np.deg2rad(angulo)
gravidade = 9.8
passo = 0.1
tempo = (2 * velocidade * np.sin(ang_rad)) / gravidade

fx = lambda t: np.abs(velocidade) * np.cos(ang_rad) * t
fy = lambda t: np.abs(velocidade) * np.sin(ang_rad) * t - ((gravidade * np.power(t, 2)) / 2)

eixos = np.array([[fx(t), fy(t)] for t in np.arange(0, tempo + passo, passo)])
x, y = eixos.T

distancia = round(np.max(x), 1)
altura_max = round(np.max(y), 1)
tempo = round(tempo, 1)

hfont = {'fontname':'Ubuntu Mono'}
fig,ax = plt.subplots(1)

fig.subplots_adjust(bottom=0.35)
fig.text(0.1,0.21,'******************************************************', hfont)
fig.text(0.1,0.16,f"Distância percorrida  ==> {distancia:8.2f} metros", hfont)
fig.text(0.1,0.11,f"Altura máxima         ==> {altura_max:8.2f} metros", hfont)
fig.text(0.1,0.06,f"Duração do lançamento ==> {tempo:8.2f} segundos", hfont)
fig.text(0.1,0.01,'******************************************************', hfont)

plt.plot(x, y, "bo")
plt.xlabel("Distância (m)")
plt.ylabel("Altura (m)")
plt.show()
