from individual import Individual

# random library
from random import randint
from random import shuffle

class Queens(Individual):
	num_queens = 8

	def __init__(self, genotype = []):
		self.genotype = genotype

	def fitness(self):
		"""
			return a double
			representing the fitness of the phenotype
		"""
		ans = 0

		# check
		for i in range(0, self.num_queens):
			for j in range(0, self.num_queens):

				# check for each previous queen
				if i != j and abs(i - j) == abs(self.genotype[i] - self.genotype[j]):
					ans = ans + 1 

		# return fitness value
		return  1 / (ans + 1)

	def mutation(self):
		"""
		realize mutation in the genotypeo
		"""

		# random select to places and swap
		gen1 = randint(0, self.num_queens - 1)
		gen2 = gen1

		# genotypeerate random number differente from previous one
		while gen1 == gen2:
			gen2 = randint(0, self.num_queens - 1)

		# swap elements
		self.genotype[gen1], self.genotype[gen2] = self.genotype[gen2], self.genotype[gen1]

	def phenotype(self):
		"""
		return the phenotype of the individual
		"""

		return self.genotype

	#
	## static or class methods
	#

	@staticmethod
	def recombination(first, second):
		""" 
		giving two parents as argument
		return a new parent with genotypes of both parents
		"""
		son = Queens([])

		# choose random point for crossover
		crossover_point = randint(1, first.num_queens - 2)

		# copy the first parent
		for i in range(0, crossover_point):
			geno = first.genotype[i]

			son.genotype.append(geno)

		# move the rest of the second parent to the son
		for j in range(0, second.num_queens):
			geno = second.genotype[j]

			if geno not in son.genotype:
				son.genotype.append(geno)

		return son

	@classmethod
	def random(cls):
		geno = list(range(1, cls.num_queens + 1))
		shuffle(geno)

		return Queens(geno)

	#
	## print methods
	#

	def  __repr__(self):
		return "Queens Obj: " + str(self.genotype)

	def __str__(self):
		return str(self.genotype)