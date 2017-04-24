## EV 
from queens import Queens
from ea import EA
from backtracking import NQueens
from survivalselection import ReplaceWorst, ReplaceAge, ReplaceFittest
from parentselection import BestParents, Tournament, Ranking, FittestBased
from permutations import Permutation
## statistic
import helper
## PyQT5
import sys

# EV algorithm params
elitism = 2
max_iter = 10000
min_fitness = 0.9
data_ite = 1

parent_selection = FittestBased()
survival_selection = ReplaceWorst(elitism)

params = {'repres' : Queens, 'p_selection' : parent_selection, 's_selection' : survival_selection,
        'pop_size' : 40, 'num_childs' : 2, 'rec_prob' : 0.9, 'mut_prob' : 0.1, 'duplicate' : False}

# initialise evolutionaru algorithm class
ea = EA(**params)

# initialise population
ea.initialise()

# search
data = ea.search(max_iter, min_fitness, data_ite)

# plot
helper.plot(data, "8-Queens GA")


# print population
sys.stdout = open("results", "w")

ea.population.sort(key=lambda x: x.fitness(), reverse=True)

for q in ea.population:
	print(q, "Fitness: " + str(q.fitness()))

## Running modifie genetic algorithm

"""
# initialise evolutionaru algorithm class
ea = EA(**params)

# initialise population
ea.initialise()

# search
data = ea.search(max_iter, min_fitness, data_ite)

# plot
helper.plot(data, "Simple GA")
"""