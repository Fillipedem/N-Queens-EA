"""
class for operator in permutations representations 
"""
from random import randint

class Permutation():

    def __init__():
        pass

    ## mutation operators
    @staticmethod
    def swap_mutation(genotype):
        new_gen = genotype.copy()

        gen1 = randint(0, len(new_gen) - 1)
        gen2 = gen1

        # genotypeerate random number differente from previous one
        while gen1 == gen2:
            gen2 = randint(0, len(new_gen) - 1)

        # swap elements
        new_gen[gen1], new_gen[gen2] = new_gen[gen2], new_gen[gen1]

        return new_gen

    @staticmethod
    def scramble_mutation(genotype):
        pass

    @staticmethod
    def inverse_mutation(genotype):
        """
        swap every element of the geno in place
        """
        new_geno = genotype.copy()

        for i in range(lenght / 2):
            new_geno[i], new_geno[len(new_geno) - i - 1] = new_geno[len(new_geno) - i - 1], new_geno[i]

        return new_geno

    ## recombination operators
    @staticmethod
    def one_point_crossover(genotype1 = [], genotype2 = []):
        child = []

        # choose random point for crossover
        crossover_point = randint(1, len(genotype1) - 2)

        # copy the first parent
        for i in range(0, crossover_point):
            geno = genotype1[i]

            child.append(geno)

        # move the rest of the second parent to the child
        for j in range(0, len(genotype2)):
            geno = genotype2[j]

            if geno not in child:
                child.append(geno)

        return child

    @staticmethod
    def n_point_crossover(genotype1 = [], genotype2 = [], n = 2):
       pass

