
# Librerias

import seaborn as sns
import matplotlib.pyplot as plt

# Datos
consumos = sns.load_dataset('tips')

# Nombres para la columna de los datos
consumos.columns = [
	'total', 'propina', 'genero', 'fumador',
	'dia', 'tipo', 'comensales'
]

print('Dataset de consumos: \n', consumos)

# Graficas

# Boxplot
sns.catplot(	
	x = 'dia', y = 'total', data = consumos, kind = 'box', col = 'fumador')
plt.show()

# Boxenplot
sns.catplot(	
	x = 'dia', y = 'total', data = consumos, kind = 'boxen', col = 'fumador')
plt.show()

# Violinplot
sns.catplot(
	x = 'dia', y = 'total', data = consumos, kind = 'violin', col = 'fumador')
plt.show()

sns.catplot(
	x = 'dia', y = 'total', data = consumos, kind = 'violin', hue = 'fumador')
plt.show()

sns.catplot(
	x = 'dia', y = 'total', data = consumos,
	kind = 'violin', hue = 'fumador', split = True
)

plt.show()