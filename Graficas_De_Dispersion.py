
# Librerias

import seaborn as sns
import matplotlib.pyplot as plt

# Datos

dataset = sns.load_dataset("penguins")

# Nombres para la columna de los datos

dataset.columns = [
	"especie", "isla", "longitud_pico", "profundidad_pico",
	"longitud_aleta", "masa", "sexo"
]

# Graficas

# Simple

sns.relplot(data = dataset, x = "longitud_pico", y = "longitud_aleta")
plt.show()

# Matiz y Tamaño Fijo

sns.relplot(data = dataset, x = "longitud_pico", y = "longitud_aleta", hue = "masa", s = 300)
plt.show()

sns.relplot(data = dataset, x = "longitud_pico", y = "longitud_aleta", hue = "especie", s = 300)
plt.show()

# Rejilla, Tamaño Personalizado y Estilo

sns.relplot(
	data = dataset, x = "longitud_pico", y = "longitud_aleta",
	hue = "especie", s = 300, row = "sexo", size = "masa", 
	sizes = (100, 500), style = "sexo", col = "isla"
)

plt.show()