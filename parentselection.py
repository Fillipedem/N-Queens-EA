from random import uniform


class ParentSelection:

    def __init__(self):
        pass

    def select_parents(self, population, num_parents):
        pass


class BestParents(ParentSelection):

    def __init__(self):
        super().__init__()

    def select_parents(self, population, num_parents = 2):
        new_parents = []

        # adding parents with the highest fitness
        for i in range(len(population)):
            
            # adding the first parents
            if len(new_parents) < num_parents:
                new_parents.append(population[i])
            else:
                # sorted by fitness
                new_parents.sort(key=lambda x: x.fitness())

                # for the rest of the parents remove the worst
                for j in range(len(new_parents)):
                    if population[i].fitness() > new_parents[j].fitness():
                        new_parents[j] = population[i]
                        break

        return new_parents

class FittestBased(ParentSelection):

    def __init__(self):
        super().__init__()

    def select_parents(self, population, num_parents = 2):
        new_parents = []

        ## create fitness list
        fitness = []
        total = 0

        for p in population:
            f = p.fitness()

            fitness.append(f)
            total += f

        # adjust
        for i in range(len(fitness)):
            fitness[i] = fitness[i]/total

            if i > 0:
                fitness[i] += fitness[i - 1]

        # wheel - search new parents
        for i in range(num_parents):
            
            r = uniform(0, 1)
            p = 0
            
            while fitness[p] < r:
                p = p + 1
            
            new_parents.append(population[p])

        return new_parents

class Tournament(ParentSelection):

    def __init__(self):
        super().__init__(elitism)

    def select_parents(self, population, num_parents = 2):
        pass

class Ranking(ParentSelection):

    def __init__(self):
        super().__init__(elitism)

    def select_parents(self, population, num_parents = 2):
        pass
