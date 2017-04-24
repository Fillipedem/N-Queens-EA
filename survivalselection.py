from random import randint
from random import uniform

class SurvivalSelection:

    def __init__():
        pass

    @staticmethod
    def select_survivals(population, offspring, parents):
        pass


class ReplaceWorst(SurvivalSelection):

    def __init__():
        pass

    @staticmethod
    def select_survivals(population, offspring, parents):
        """
        remove the lowest element in population
        """
        new_pop = []

        for i in population:
            offspring.append(i)

        # sorted offspring by highest fitness
        offspring.sort(key=lambda x: x.fitness(), reverse=True)

        for i in range(len(population)):
            new_pop.append(offspring[i])

        return new_pop


class ReplaceFittest(SurvivalSelection):

    def __init__():
        pass

    @staticmethod
    def select_survivals(population, offspring, parents):
        new_pop = []

        for i in offspring:
            new_pop.append(i)

        # adding the rest of the population
        for i in population:
            new_pop.append(i)

        ## create fitness list of the actual population
        fitness = []
        total = 0

        for off in population:
            f = off.fitness()

            fitness.append(1/(1 + f))
            total += 1/(1 + f)

        # adjust
        for i in range(len(fitness)):
            fitness[i] = fitness[i]/total

            if i > 0:
                fitness[i] += fitness[i - 1]

        # wheel - search new survivals
        i = 0
        while i < len(offspring):
            
            r = uniform(0, 0.999999)
            p = 0
            
            while fitness[p] < r:
                p = p + 1
            
            if population[p] in new_pop:
                new_pop.remove(population[p])
            else:
                i = i - 1

            i = i + 1    

        return new_pop

class ReplaceAge(SurvivalSelection):

    def __init__():
        pass

    @staticmethod
    def select_survivals(population, offspring, parents):
        pass