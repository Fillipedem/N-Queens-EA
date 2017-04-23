from queens import Queens
from ea import EA
from backtracking import NQueens
from survivalselection import SurvivalFittest
from parentselection import BestParents

import helper
import sys

sys.stdout = open('test', 'w')

def printa(ea):
	print("\n\n")
	print("Geração: ")
	print("Population ", ea.population)
	print("Parents: ", ea.parents)

f = open('test', 'w')

# population types
pop_size = 10
num_childs = 2
rec_prob = 0.9
mut_prob = 0.2

# ev type
repre = Queens
s_selection = SurvivalFittest
p_selection = BestParents

ea = EA(repre, p_selection, s_selection, pop_size, num_childs, rec_prob, mut_prob)

ea.initialise()
printa(ea)

for i in range(6):
	ea.run()
	printa(ea)



"""
ea.search(2000, 1)
print("Search")
print(helper.med(ea.population), helper.dev(ea.population), helper.var(ea.population))

printa(ea)
"""