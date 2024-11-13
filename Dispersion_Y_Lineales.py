
from Dataset_Pinguinos import *

# Gráfico de líneas
sns.lineplot(
    x = "longitud_pico", 
    y = "longitud_aleta", 
    data = dataset, 
    hue = "especie"
)
plt.show()