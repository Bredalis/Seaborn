
from Dataset_Tips import *

# Función para graficar datos categóricos
def graficas_categoricas(y, tipo, columna, leyenda):
    sns.catplot(
        x = "dia", y = y, data = consumos, kind = tipo,
        col = columna, hue = leyenda
    )
    plt.show()

# Ejemplos de uso de la función
graficas_categoricas("total", "point", "fumador", None)
graficas_categoricas("total", "bar", None, "comensales")
graficas_categoricas(None, "count", None, "comensales")