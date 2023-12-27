
# Librerias

import seaborn as sns
import matplotlib.pyplot as plt

# Datos
dataset = sns.load_dataset('penguins')

# Nombres para la columna de los datos
dataset.columns = [
	'especie', 'isla', 'longitud_pico', 'profundidad_pico',
	'longitud_aleta', 'masa', 'sexo'
]

# Grafica
sns.relplot(
	data = dataset, x = 'especie', y = 'masa', kind = 'line',
	hue = 'sexo', style = 'sexo', errorbar = 'sd')
plt.show()