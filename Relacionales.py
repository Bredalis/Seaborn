
from Dataset_Pinguinos import *

# Estilo de la grafica

sns.set_theme(style = "darkgrid", context = "talk")

relacional = sns.relplot(
	data = dataset, height = 7, 
	aspect = 1.2, markers = ["s", ".", "P", "d"] 
)

relacional.set(title = "Analisis de Pinguinos")
relacional.set_xlabels("Numeros de Pinguinos")
relacional.set_ylabels("Variables")

plt.show()