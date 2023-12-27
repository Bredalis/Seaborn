
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

print('Dataset de consumos: \n', consumos)

# Graficas

# Pointplot
sns.catplot(
	x = 'dia', y = 'total', data = consumos, kind = 'point', col = 'fumador')
plt.show()

# Barplot
sns.catplot(
	x = 'dia', y = 'total', data = consumos, kind = 'bar', hue = 'comensales')
plt.show()

# Countplot
sns.catplot(x = 'dia', data = consumos, kind = 'count', hue = 'comensales')
plt.show()