from individual import Individual

# random library
from random import randint
from random import shuffle
# sqrt
from math import sqrt, pow

#
from permutations import Permutation

class Queens(Individual):
    num_queens = 8
    mutate = Permutation.swap_mutation
    crossover = Permutation.one_point_crossover

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

        ans = ans / 2

        # return fitness value
        return  1 / (ans + 1)

    def mutation(self):
        """
        makes mutatation in the genotype
        """
        new_geno = Permutation.swap_mutation(self.genotype)
       
        return Queens(new_geno)

    def phenotype(self):
        """
        return the phenotype of the individual
        """

        return self.genotype

    #
    ## static or class methods
    #

    @classmethod
    def recombination(cls, first, second):
        """ 
        giving two parents as argument
        return a new parent with genotypes of both parents
        """
        child1, child2 = cls.crossover(first.genotype, second.genotype)

        return Queens(child1), Queens(child2)

    @classmethod
    def random(cls):
        geno = list(range(1, cls.num_queens + 1))
        shuffle(geno)

        return Queens(geno)

    #
    ## change the mutation and recombination methods
    #
    @classmethod
    def set_new_mutation(cls, mutate):
        cls.mutate = mutate
    
    @classmethod
    def set_new_recombination(cls, crossover):
  	   cls.crossover = crossover

    #
    ## print methods
    #
    def  __repr__(self):
        return "Queens Obj: " + str(self.genotype)

    def __str__(self):
        return str(self.genotype)


    #
    ## default operator
    #
    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.genotype == other.genotype

        return False