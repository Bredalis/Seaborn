
from Dataset_Tips import *

# Gráficas categóricas
def graficas_categoricas(tipo):
    sns.catplot(
        x = "dia", y = "total", data = consumos, 
        hue = "comensales", s = 7, col = "fumador", kind = tipo
    )
    plt.show()

# Generar gráficos de tipo 'strip' y 'swarm'
graficas_categoricas("strip")
graficas_categoricas("swarm")