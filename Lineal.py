
from Dataset_Pinguinos import *

# Grafica
sns.relplot(
	data = dataset, x = "especie", y = "masa", kind = "line",
	hue = "sexo", style = "sexo", errorbar = "sd")
plt.show()