

class ParentSelection:

    def __init__():
        pass

    @staticmethod
    def select_parents(population = [], num_parents):
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
                new_parents.append(self.population[i])
            else:
                # for the rest of the parents remove the worst
                for j in range(len(new_parents)):
                    if population[i].fitness() > new_parents[j].fitness():
                        self.parents[j] = self.population[i]
                        break

        return new_parents