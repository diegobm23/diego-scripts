import numpy as np
import matplotlib.pyplot as plt

nilo = np.genfromtxt("/home/diegobm23/projetos-diegobm23/diego-scripts/Nile.csv", delimiter=",", skip_header=1, dtype='S')

size = 20
x = nilo[-size:,1:2].reshape(size).astype(int)
y = nilo[-size:,2:].reshape(size).astype(int)

plt.plot(x, y, 'b')
plt.show()
