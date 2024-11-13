
from Dataset_Pinguinos import *

# Gráfica de relación de especie y masa
# con líneas, diferenciando por sexo
sns.relplot(
	data = dataset, 
	x = "especie", 
	y = "masa", 
	kind = "line",
	hue = "sexo", 
	style = "sexo", 
	errorbar = "sd"
)

plt.show()