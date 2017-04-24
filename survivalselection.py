from random import randint
from random import uniform

class SurvivalSelection:

    def __init__(self, elitism = 8):
        self.elitism = 8

    def set_elitism(self, elitism):
        cls.elitism = 8

    def select_survivals(self, population, offspring, parents):
        pass


class ReplaceWorst(SurvivalSelection):

    def __init__(self, elitism):
        super().__init__(elitism)

    def select_survivals(self, population, offspring, parents):
        """
        remove the lowest element in population
        """
        new_pop = []

        for i in population:
            new_pop.append(i)

        # sorted offspring by highest fitness
        new_pop.sort(key=lambda x: x.fitness())

        for i in range(len(offspring)):
            ## check if is not in the population
            if offspring[i] in new_pop:
                continue

            for j in range(len(population)):

                if offspring[i].fitness() > new_pop[i].fitness():
                    new_pop[i] = offspring[i]

                    break

        return new_pop


class ReplaceFittest(SurvivalSelection):

    def __init__(self, elitism):
        super().__init__(elitism)

    def select_survivals(self, population, offspring, parents):
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

            fitness.append(1/(1 + f*self.elitism))
            total += 1/(1 + f*self.elitism)

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

    def __init__(self, elitism):
        super().__init__(elitism)

    def select_survivals(self, population, offspring, parents):
        new_pop = []

        # adding the rest of the population
        for i in population:
            new_pop.append(i)


        offspring.sort(key=lambda x: x.fitness(), reverse = True)
        # remove parents
        for i in range(len(parents)):
            if parents[i] in new_pop:

                for j in offspring:
                    if j not in new_pop:
                        new_pop.append(j)
                        new_pop.remove(parents[i])
                        break

        return new_pop