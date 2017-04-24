## EV 
from queens import Queens
from ea import EA
from backtracking import NQueens
from survivalselection import ReplaceWorst, AgeBased
from parentselection import BestParents, Tournament, Ranking
## statistic
import helper
## PyQT5
import sys

# EV algorithm params
params = {'repres' : Queens, 'p_selection' : BestParents, 's_selection' : ReplaceWorst,
        'pop_size' : 100, 'num_childs' : 10, 'rec_prob' : 0.9, 'mut_prob' : 0.005}

max_iter = 1000
min_fitness = 0.8
data_ite = 1

# initialise evolutionaru algorithm class
ea = EA(**params)

# initialise population
ea.initialise()

# search
data = ea.search(max_iter, min_fitness, data_ite)

# plot
helper.plot(data, "Simple GA")

print(ea.population)
for i in ea.population:
	print(i.fitness(), end=" ")

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