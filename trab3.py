from random import randrange
from numpy import *

class tabuleiro:
	def __init__(self,N,x):
		self.boards = zeros((x,N,N),dtype=int)  # Array 3d com dimensões x, N, N
		self.N = N
		self.x = x
		for i in range(x): # coloca as rainhas
			j = 0
			while j < N:
				a,b = randrange(N),randrange(N)
				if self.boards[i,a,b] != 1: # garante que nao seleciona duas rainhas pro mesmo quadrado
					self.boards[i,a,b] = 1
					j+=1
	
	def show(self):  # função de print
		for i in range(self.x):
			for j in range(self.N):
				for k in range(self.N):
					print(self.boards[i][j][k]," ",end="")
				print()
			print("---"*self.N)


def todosVizinhos(tab):
	N = len(tab)
	for i in range(N):
		pass



def main():
		
	tab = tabuleiro(4,5)
	tab.show()
	todosVizinhos(tab.boards[0])

if __name__ == "__main__":
	main()
