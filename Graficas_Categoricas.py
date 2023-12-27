
# Librerias

import seaborn as sns
import matplotlib.pyplot as plt

# Datos
consumos = sns.load_dataset('tips')

# Nombres para la columna de los datos
consumos.columns = [
	'total', 'propia', 'genero', 'fumador',
	'dia', 'tipo', 'comensales'
]

print('Dataset de consumos:', consumos)

# Graficas

# Stripplot
sns.catplot(
	x = 'dia', y = 'total', data = consumos, 
	hue = 'comensales', s = 7, col = 'fumador')
plt.show()

# Swarm
sns.catplot(
	x = 'dia', y = 'total', data = consumos, 
	hue = 'comensales', s = 7, col = 'fumador', kind = 'swarm')
plt.show()