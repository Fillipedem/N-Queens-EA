#
# backtracking solution for the N-Queens Problem
#

class NQueens:

	def __init__(self):
		self.pop_size = 0
		self.num_queens = 0
		self.population = []


	def generate(self, num_queens, pop_size):
		# clear
		self.population = []
		self.num_queens = num_queens
		self.pop_size = pop_size

		# generate
		self.__backtraking([], 0)

		return self.population
		

	def __backtraking(self, A, current):

		# stop iteration
		if len(self.population) >= self.pop_size:
			return None
		
		if current == self.num_queens:
			self.population.append(A)
			return None

		# checando proximo estado possivel
		for i in range(1, self.num_queens + 1):

			# checando choques com rainhas anteriores
			shock = False
			for j in range(0, current):

				if i == A[j] or abs(i - A[j]) == abs(current - j):
					shock = True
					break

			# se não houver choques
			if not shock:
				self.__backtraking(A + [i], current + 1)


