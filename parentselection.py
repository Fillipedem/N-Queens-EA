

class ParentSelection:

    def __init__():
        pass

    @staticmethod
    def select_parents(population, num_parents):
        pass



class BestParents(ParentSelection):

    def __init__():
        pass

    @staticmethod
    def select_parents(population, num_parents = 2):
        new_parents = []

        # adding parents with the highest fitness
        for i in range(len(population)):
            
            # adding the first parents
            if len(new_parents) < num_parents:
                new_parents.append(population[i])
            else:
                # sorted by fitness
                sorted(new_parents, key=lambda x: x.fitness())

                # for the rest of the parents remove the worst
                for j in range(len(new_parents)):
                    if population[i].fitness() > new_parents[j].fitness():
                        new_parents[j] = population[i]
                        break

        return new_parents


class Tournament(ParentSelection):

    def __init__():
        pass

    @staticmethod
    def select_parents(population, num_parents = 2):
        pass

class Ranking(ParentSelection):

    def __init__():
        pass

    @staticmethod
    def select_parents(population, num_parents = 2):
        pass
