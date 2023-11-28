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

		for p in perms:
			if not self.contains(p,pattern):
				self.notcontaining.append(p)

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

	def getList(self):
		return notcontaining

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

		result_list = PatternAvoid(n,pattern).getList()

		result_str = "\nThe following "+str(len(result_list))+" are all the " + str(n)+"-permutations not containing the pattern " 
		result_str = result_str + str_pattern+":\n\n"+printlist(result_list)

		print(result_str)

		result_file = open("./log/"+str(n)+"Av"+str_pattern+".txt","w")
		result_file.write(result_str+"\n")
		result_file.close()
	
	else:
		# for future implementation of GUI interface
		print("GUI not implemented yet, use command line")
