# Class for Evolutionary Algorithm
from random import randint
import helper 

class EA:
    num_parents = 2

    def __init__(self, repres, p_selection, s_selection,
                pop_size = 5, num_childs = 2, rec_prob = 0.9, mut_prob = 0.2):

        # represeting the individuals
        self.population = []
        self.parents = []
        self.offspring = []

        # type of the evolutionary algorithm
        self.representation = repres
        self.p_selection = p_selection
        self.s_selection = s_selection

        # population details
        self.pop_size = pop_size
        self.num_childs = num_childs
        self.rec_prob = rec_prob
        self.mut_prob = mut_prob

    ##
    ## Evolutionary Algorithm phases
    ##
    def initialise(self):
        # clear old population
        self.population = []
        self.parents = []
        self.offspring = []

        # random generate initial population
        for i in range(0, self.pop_size):
            new = self.representation.random()
            self.population.append(new)

    def run(self):
        """
        Run one generation
        """

        # parent selection
        self.__parent_selection()

        # recombination
        self.__recombination()
        
        # mutation
        self.__mutation()

        # survivor selection
        self.__survivor_selector();

    def search(self, max_iter, min_fitness, save_ite):
        """
        runs the evolutonary algorithm
        with max_iter and min_fitness as a "stop criter"
        
        returns the list of tuples (num_ite, [populaton_data])
        """
        num_ite = 0
        data_ite = 0
        m, s, v = self.get_population_data()
        data = ([num_ite], [m], [s], [v])


        for i in range(max_iter):
            num_ite = num_ite + 1
            data_ite = data_ite + 1

            pop_fitness = helper.med(self.population)

            if pop_fitness > min_fitness: # check if we get the min_fitness
                m, s, v = self.get_population_data()

                data[1].append(m)
                data[2].append(s)
                data[3].append(v)
                data[0].append(num_ite)
                break
            else:
                self.run()

            # check with we add data to the ans
            if data_ite == save_ite:
                m, s, v = self.get_population_data()

                data[1].append(m)
                data[2].append(s)
                data[3].append(v)
                data[0].append(num_ite)

                data_ite = 0



        return data

    def get_population_data(self):
        """
        return de media, standard deviation and variance of the actual population
        """
        data = helper.med(self.population), helper.dev(self.population), helper.var(self.population)

        return data

    # ea componentes
    def __parent_selection(self):
        """
        select new parents from population
        """
        self.parents = self.p_selection.select_parents(self.population, self.num_parents)


    def __recombination(self):
        """
        make crossover to create new candidates 
        """
        self.offspring = []

        # parents
        first = self.parents[0]
        second = self.parents[1]

        for i in range(self.num_childs):
            new_son = self.representation.recombination(first, second)

            self.offspring.append(new_son)

        # adding population
        for c in self.population:
            self.offspring.append(c)


    def __mutation(self):
        """
        mutate an element of the offspring
        """
        for i in range(len(self.offspring)):
            r = randint(0, 9)

            if (r < self.mut_prob):
                self.offspring[i].mutation()

    def __survivor_selector(self):
        """
        remove the lowest element in population
        """
        new_pop = self.s_selection.select_survivals(self.offspring, self.pop_size)

        self.population = new_pop

