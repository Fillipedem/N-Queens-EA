## Plot Libraries
import matplotlib.pyplot as plt
import numpy as np
## EV 
from queens import Queens
from ea import EA
from backtracking import NQueens
from survivalselection import SurvivalFittest
from parentselection import BestParents
## statistic
import helper


## main interface ##


# EV algorithm params
params = {'repres' : Queens, 'p_selection' : BestParents, 's_selection' : SurvivalFittest,
		'pop_size' : 20, 'num_childs' : 2, 'rec_prob' : 0.9, 'mut_prob' : 0.2}

max_iter = 100
min_fitness = 0.9
data_ite = 10


# initialise evolutionaru algorithm class
ea = EA(**params)

# initialise population
ea.initialise()

# search
data = ea.search(max_iter, min_fitness, data_ite)

## Plot results ##
plt.plot(data[0], data[1], label='Media')
plt.plot(data[0], data[2], label='Standard Variation')
plt.plot(data[0], data[3], label='Variance')

plt.xlabel('Iteration')
plt.ylabel('Fitness')

plt.title("NQueens EV")

plt.legend()

plt.show()