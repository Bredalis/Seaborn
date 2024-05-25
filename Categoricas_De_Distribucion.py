
from Dataset_Tips import *

# Graficas

def graficas_categoricas(tipo, leyenda = None):

	sns.catplot(	
	x = "dia", y = "total", data = consumos, kind = tipo, 
	col = "fumador", hue = leyenda)
	plt.show()

graficas_categoricas("box")
graficas_categoricas("boxen")
graficas_categoricas("violin")
graficas_categoricas("violin", "fumador")