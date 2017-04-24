from random import randint


class SurvivalSelection:

    def __init__():
        pass

    @staticmethod
    def select_survivals(offspring, num_population):
        pass


class ReplaceWorst(SurvivalSelection):

    def __init__():
        pass

    @staticmethod
    def select_survivals(offspring, num_population):
        """
        remove the lowest element in population
        """
        new_pop = []

        # sorted offspring by highest fitness
        offspring.sort(key=lambda x: x.fitness(), reverse=True)

        for i in range(num_population):
            new_pop.append(offspring[i])

        return new_pop


class AgeBased(SurvivalSelection):

    def __init__():
        pass

    @staticmethod
    def select_survivals(offspring, num_population):
        pass