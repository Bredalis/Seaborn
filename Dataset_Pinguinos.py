
# Librerías
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
dataset = sns.load_dataset("penguins")

# Asignar nombres a las columnas
dataset.columns = [
    "especie", "isla", "longitud_pico", "profundidad_pico",
    "longitud_aleta", "masa", "sexo"
]

# Mostrar el dataset
print("Dataset de Pinguinos:\n", dataset)