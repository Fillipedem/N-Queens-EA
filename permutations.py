"""
class for operator in permutations representations 
"""
from random import randint
from random import shuffle

class Permutation():

    def __init__():
        pass

    ## mutation operators
    @staticmethod
    def swap_mutation(genotype):
        # search two points to swap
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

        # search the two points for scramble
        gen1 = randint(0, len(new_gen) - 1)
        gen2 = gen1

        # genotypeerate random number differente from previous one
        while gen1 == gen2:
            gen2 = randint(0, len(new_gen) - 1)

        tmp = []
        gen1, gen2 = min(gen1, gen2), max(gen1, gen2)
        for i in range(gen1, gen2):
            tmp.append(genotype[i])


        shuffle(tmp)

        new_geno = []
        for i in range(len(genotype)):
            if i in range(gen1, gen2):
                new_geno.append(tmp[i])
            else:
                new_geno.append(genotype[i])


        return new_geno

    @staticmethod
    def inverse_mutation(genotype):
        """
        swap every element of the geno in place
        """
        
        return genotype[::-1]

    ## recombination operators
    @staticmethod
    def one_point_crossover(genotype1 = [], genotype2 = []):
        child = []
        second_child = []

        # choose random point for crossover
        crossover_point = randint(1, len(genotype1) - 2)

        # copy the first parent
        for i in range(0, crossover_point):

            child.append(genotype1[i])
            second_child.append(genotype2[i])

        # move the rest of the second parent to the child
        for j in range(0, len(genotype2)):
            geno = genotype2[j]

            if geno not in child:
                child.append(geno)

            geno = genotype1[j]

            if geno not in second_child:
                second_child.append(geno)

        return child, second_child

    @staticmethod
    def n_point_crossover(genotype1 = [], genotype2 = [], n = 2):
       pass

