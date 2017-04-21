from statistics import variance, stdev, mean


def med(population):
	"""
	population med
	"""
	m = []

	for c in population:
		m.append(c.fitness())


	return mean(m)


def dev(population):
	"""
	Population standard deviation
	"""
	m = []

	for c in population:
		m.append(c.fitness())


	return stdev(m)

def var(population):
	"""
	variance
	"""
	m = []

	for c in population:
		m.append(c.fitness())

	return variance(m)