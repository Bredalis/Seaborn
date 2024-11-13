
from Dataset_Pinguinos import *

# Configuración del estilo de la gráfica
sns.set_theme(style = "darkgrid", context = "talk")

# Creación de la gráfica relacional
relacional = sns.relplot(
	data = dataset, height = 7,
	aspect = 1.2, markers = ["s", ".", "P", "d"] 
)

# Configuración de títulos y etiquetas
relacional.set(title = "Análisis de Pinguinos")
relacional.set_xlabels("Números de Pinguinos")
relacional.set_ylabels("Variables")

plt.show()