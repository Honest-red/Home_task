a = [
	[34587, 'Learning Python, Mark Lutz', 4, 40.95],
	[98762, 'Programming Python, Mark Lutz', 5, 56.80],
	[77226, 'Head First Python, Paul Barry', 3, 32.95],
	[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

from pprint import pprint


def fuk(a):
	return a[3]*a[2]


def fun(a):
	cc = fuk(a)
	if cc  < 100:
		cc = cc + 10
		print()
	return [a[0], round(cc)]

print(list(map(fun, a)))