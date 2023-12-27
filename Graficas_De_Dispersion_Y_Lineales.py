
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

# Graficas

figura, ejes = plt.subplots(1, 2, figsize = (15, 5)) 

# Lineas
sns.lineplot(
	data = dataset, x = 'longitud_pico', y = 'longitud_aleta',
	hue = 'especie', size = 'masa', sizes = (50, 50), 
	style = 'sexo', ax = ejes[0]
)

# Dispersion
sns.scatterplot(
	data = dataset, x = 'especie', y = 'masa',
	hue = 'sexo', style = 'sexo', ax = ejes[1]
)

plt.show()