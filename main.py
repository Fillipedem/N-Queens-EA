from queens import Queens
from ea import EA

def printa(ea):
	print("Population ", ea.population)
	print("Parents: ", ea.parents)

pop_size = 5
kind = Queens

ea = EA(kind, pop_size)



ea.initialise()


ea.run()
ea.run()
ea.run()
ea.run()
ea.run()
ea.run()

printa(ea)



