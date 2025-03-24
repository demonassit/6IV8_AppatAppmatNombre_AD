import numpy as np
import matplotlib.pyplot as plt

#vamos a crear una semilla random
np.random.seed(0)

#vamos a obtener los parametros que necesitamos para la distribucion normal

media = 0
sigma1 = 1
sigma2 = 2
sigma3 = 3
n_muestras = 1000

#generar la disribucion
data1 = np.random.normal(media, sigma1, n_muestras)
data2 = np.random.normal(media, sigma2, n_muestras)
data3 = np.random.normal(media, sigma3, n_muestras)

#configurar el grafico
plt.figure(figsize=(10,6))

#graficarlo como un histograma
plt.hist(data1, bins=30, color='blue', density=True, label='Desviacion Estandar : 1', alpha=0.5)
plt.hist(data2, bins=30, color='red', density=True, label='Desviacion Estandar : 2', alpha=0.5)
plt.hist(data3, bins=30, color='green', density=True, label='Desviacion Estandar : 3', alpha=0.5)

#formato a la grafica
plt.title('Comparacion de Distribuciones Estandar con una semilla random')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()
plt.grid()

plt.show()