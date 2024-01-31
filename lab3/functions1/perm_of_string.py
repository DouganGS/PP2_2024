import itertools

def permutations(string): # 'abc'
	perms = [''.join(p) for p in itertools.permutations(string)] # a b c
	print(perms)

permutations("abc")