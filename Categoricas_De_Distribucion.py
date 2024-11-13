
from Dataset_Tips import * 

# Gráficas categóricas
def graficas_categoricas(tipo, leyenda = None):
    sns.catplot(
        x = "dia", y = "total", data = consumos, kind = tipo, 
        col = "fumador", hue = leyenda
    )
    plt.show()

# Generar diferentes tipos de gráficos
graficas_categoricas("box")
graficas_categoricas("boxen")
graficas_categoricas("violin")
graficas_categoricas("violin", "fumador")