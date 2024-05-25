
# Librerias

import seaborn as sns
import matplotlib.pyplot as plt

# Datos
consumos = sns.load_dataset("tips")

# Nombres para la columna de los datos
consumos.columns = [
	"total", "propina", "genero", "fumador",
	"dia", "tipo", "comensales"
]

print("Dataset de consumos: \n", consumos)