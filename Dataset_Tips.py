
# Librerías
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
consumos = sns.load_dataset("tips")

# Asignar nombres a las columnas
consumos.columns = [
	"total", "propina", "genero", "fumador",
	"dia", "tipo", "comensales"
]

# Mostrar el dataset
print("Dataset de consumos:\n", consumos)