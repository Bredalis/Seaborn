
from Dataset_Pinguinos import *

# Graficas

# Lineas
sns.lineplot(
    x = "longitud_pico", y = "longitud_aleta", 
    data = dataset, hue = "especie")
plt.show()