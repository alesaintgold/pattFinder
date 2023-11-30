import sys
import tkinter as tk
from itertools import permutations
from itertools import combinations

class PatternAvoid(object):
	def __init__(self,n, pattern ):
		if n <= 1:
			print("ERROR: expecting a whole number grater than 1 but got: " + str(n))
			exit()

		for i in range(1, len(pattern)):
			if i not in pattern:
				print("ERROR: expected a pattern but got: " + str(pattern))
				print("\nA pattern of lenght n must have all the numbers from 1 to n, " + str(i) + " not present")
				exit()

		perms = list(permutations(range(1,n+1)))

		self.notcontaining = []
		self.containing = []

		for p in perms:
			if not self.contains(p,pattern):
				self.notcontaining.append(p)
			else:
				self.containing.append(p)

	def patternize(self,pi):
		output = []
		sortedpi = sorted(pi)
		for p in pi:
			output.append(sortedpi.index(p)+1)
		return output

	def contains(self, seq, pattern):
		subseq = combinations(seq, len(pattern))

		for s in subseq:
			if self.patternize(s) == pattern:
				return True

		return False

	def getNotContaining(self):
		return self.notcontaining

	def getContaining(self):
		return self.containing

def printlist(list):
	result = ""
	for item in list:
		result = result +(str(item) + "\n")
	return result

if __name__ == '__main__':

	narg = len(sys.argv)
	
	if narg not in (1,3):
		print("ERROR: unexpected number of arguments")
		exit()

	if(narg==3):
		n = int(sys.argv[1])	 
		str_pattern = sys.argv[2]
		pattern = [int(char) for char in str_pattern]

		pa = PatternAvoid(n,pattern)

		con = pa.getContaining()
		ncon = pa.getNotContaining()

		ncon_str = "\nThe following "+str(len(ncon))+" " + str(n)+"-permutations do not contain the pattern " + str_pattern+":\n\n"+printlist(ncon)
		con_str = "\nThe following "+str(len(con))+" " + str(n)+"-permutations do contain the pattern "  + str_pattern+":\n\n"+printlist(con)

		print(ncon_str+"\n")
		print(con_str)

		# only the not conatining get saved in a file
		result_file = open("./log/"+str(n)+"Av"+str_pattern+".txt","w")
		result_file.write(ncon_str+"\n")
		result_file.close()
	
	else:
		# for future implementation of GUI interface
		print("GUI not implemented yet, use command line")
