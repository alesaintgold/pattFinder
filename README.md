x# patternFinder
this software can be used to look for meta pattern within whole numbers permutations 

Input:	int n, meta-pattern description
Output:	list of n-permutations that avoid the pattern 

steps:
	1. generating all the n-permutations (this part can be copied from permutasort)
	2. scrolling every permutations, deleting those who contain the pattern
		2a. for every permutations looking for every sub-sequence (even non consecutive)
		2b. reduce every subsequence to a pattern (the minimum value to 1, the second minumun to 2,...)
		2c. confront all of them with the pattern 

Stuff that I need:
	* function that reduce a sequence to a pattern