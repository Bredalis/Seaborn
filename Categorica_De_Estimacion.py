
from Dataset_Tips import *

# Graficas

def graficas_categoricas(y, tipo, columna, leyenda):
	sns.catplot(
		x = "dia", y = y, data = consumos, kind = tipo, 
		col = columna, hue = leyenda)
	plt.show()

graficas_categoricas("total", "point", "fumador", None)
graficas_categoricas("total", "bar", None, "comensales")
graficas_categoricas(None, "count", None, "comensales")