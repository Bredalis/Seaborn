
from Dataset_Tips import *

# Graficas

def graficas_categoricas(tipo):

	sns.catplot(
	x = "dia", y = "total", data = consumos, 
	hue = "comensales", s = 7, col = "fumador", kind = tipo)
	plt.show()

graficas_categoricas("strip")
graficas_categoricas("swarm")