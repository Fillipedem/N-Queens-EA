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

        # return fitness value
        return  (1 / (ans + 1))**0.5

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
        new_geno = cls.crossover(first.genotype, second.genotype)

        return Queens(new_geno)

    @classmethod
    def random(cls):
        geno = list(range(1, cls.num_queens + 1))
        shuffle(geno)

        return Queens(geno)

    #
    ## change the mutation and recombination methods
    #
    def set_new_mutation(mutate):
        self.mutate = mutate

    def set_new_recombination(crossover):
  	   self.crossover = crossover

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