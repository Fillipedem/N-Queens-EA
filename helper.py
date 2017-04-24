from statistics import variance, stdev, mean
## Plot Libraries
import matplotlib.pyplot as plt
import numpy as np

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


def plot(data, title):
    """
	plot results from a EV algorithm search
    """
    plt.plot(data[0], data[1], label='Média')
    plt.plot(data[0], data[2], label='Desvio Padrão')
    plt.plot(data[0], data[3], label='Variância')

    plt.xlabel('Iteration')
    plt.ylabel('Fitness')

    plt.title(title)

    plt.legend()

    plt.show()