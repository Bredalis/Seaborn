
from Dataset_Pinguinos import *

# Lineas

sns.lineplot(
    x = "longitud_pico", y = "longitud_aleta", 
    data = dataset, hue = "especie")
plt.show()