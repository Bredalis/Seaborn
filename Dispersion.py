
from Dataset_Pinguinos import *

# Graficas

def graficas_dispersion(leyenda, tamaño, fila = None, magnitud = None, 
	magnitudes = None, estilo = None, columna = None):

	sns.relplot(data = dataset, x = "longitud_pico", y = "longitud_aleta",
		hue = leyenda, s = tamaño, row = fila, size = magnitud, 
	sizes = magnitudes, style = estilo, col = columna)
	plt.show()

graficas_dispersion(None, None) # Simple 
graficas_dispersion("masa", 300) # Matiz y Tamaño Fijo 
graficas_dispersion("especie", 300)
graficas_dispersion("especie", 300, "sexo", 
	"masa", (100, 500), "sexo", "isla") # Rejilla, Tamaño Personalizado y Estilo