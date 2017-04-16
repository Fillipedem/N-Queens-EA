# Class for Evolutionary Algorithm

class EA:
    num_parents = 2
    mutation_prob = 0.0001

    def __init__(self, kind, pop_size):
        # represeting the individuals
        self.population = []
        self.parents = []
        self.offspring = []

        # type of evolutionary algorithm
        self.kind = kind

        # population details
        self.pop_size = pop_size

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
            new = self.kind.random()
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

    def search(self, max_iter, min_fitness):
        """
        runs the evolutonary algorithm
        with max_iter and min_fitness as a "stop criter"
        """
        num_ite = 0

        for i in range(max_iter):
            num_ite = num_ite + 1

            pop_fitness = map(lambda x: x.fitness(), self.population)

            if max(pop_fitness) > min_fitness: # check if we get the min_fitness
                break
            else:
                self.run()

        return num_ite

    # ea componentes
    def __parent_selection(self):
        """
        select new parents from population
        """
        self.parents = []

        ## adding parents with the highest fitness
        for i in range(len(self.population)):
            if len(self.parents) < self.num_parents:
                self.parents.append(self.population[i])
            else:
                for j in range(len(self.parents)):
                    if self.population[i].fitness() > self.parents[j].fitness():
                        self.parents[j] = self.population[i]
                        break


    def __recombination(self):
        """
        make crossover to create new candidates 
        """
        self.offspring = []

        # parents
        first = self.parents[0]
        second = self.parents[1]

        for i in range(self.pop_size):
            new_son = self.kind.recombination(first, second)

            self.offspring.append(new_son)

    def __mutation(self):
        """
        mutate an element of the offspring
        """
        for i in range(len(self.offspring)):
            pass

    def __survivor_selector(self):
        new_pop = []

        for i in self.offspring:
            new_pop.append(i)

        self.population = new_pop