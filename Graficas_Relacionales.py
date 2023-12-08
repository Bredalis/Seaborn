
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

print("dataset de Pinguinos: \n", dataset)

# Grafica

sns.set_theme(style = "darkgrid", context = "talk")

relacional = sns.relplot(
	data = dataset, height = 7, 
	aspect = 1.2, markers = ["s", ".", "P", "d"] 
)

relacional.set(title = "Analisis de Pinguinos")
relacional.set_xlabels("Numeros de Pinguinos")
relacional.set_ylabels("Variables")

plt.show()