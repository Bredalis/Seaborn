
# Librerías

import seaborn as sns
import matplotlib.pyplot as plt

dataset = sns.load_dataset("penguins")

# Nombres para la columna de los datos

dataset.columns = [
	"especie", "isla", "longitud_pico", "profundidad_pico",
	"longitud_aleta", "masa", "sexo"
]

print("Dataset de Pinguinos: \n", dataset)