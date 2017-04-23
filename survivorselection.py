from random import randint


class SurvivalSelection:

    def __init__():
        pass

    @staticmethod
    def select_survivor(offpsring = [], num_survival):
        pass


class SurvivalFittest(SurvivalSelection):

    def __init__():
        pass


    @staticmethod
    def select_survivor(offpsring, num_survival):
        """
        remove the lowest element in population
        """
        new_pop = []

        # sorted offspring by highest fitness
        sorted(offspring, key=lambda x: x.fitness(), reverse=True)

        for i in range(num_survival):
            new_pop.append(offspring[i])

        return new_pop
