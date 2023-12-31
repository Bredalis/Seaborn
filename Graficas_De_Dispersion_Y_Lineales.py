
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
    x = 'bill_length_mm', y = 'flipper_length_mm', 
    data = dataset, hue = 'species')
plt.show()

# Dispersion
sns.scatterplot(
    x = 'species', y = 'body_mass_g', data = dataset, 
    hue = 'sex')
plt.show()