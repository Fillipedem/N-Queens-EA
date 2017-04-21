from queens import Queens
from ea import EA
from backtracking import NQueens
import helper
import sys

sys.stdout = open('test', 'w')


def printa(ea):
	print("\n\n")
	print("Geração: ")
	print("Population ", ea.population)
	print("Parents: ", ea.parents)

f = open('test', 'w')

pop_size = 10
num_childs = 2
rec_prob = 0.9
mut_prob = 0.2
kind = Queens

ea = EA(kind, pop_size, num_childs, rec_prob, mut_prob)

ea.initialise()


##ea.search(2000,1)
##print("Search")
##print(helper.med(ea.population), helper.dev(ea.population), helper.var(ea.population))

queens = NQueens()

print(queens.generate(16, 5))

for i in queens.generate(8, 5):
	print(Queens(i).fitness())

