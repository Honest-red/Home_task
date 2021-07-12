a = [
	[34587, 'Learning Python, Mark Lutz', 4, 40.95],
	[98762, 'Programming Python, Mark Lutz', 5, 56.80],
	[77226, 'Head First Python, Paul Barry', 3, 32.95],
	[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

from pprint import pprint
pprint(list(map(lambda a:(lambda a: a[3]*a[2] < 100, [a[0], round(a[3]*a[2]+10)]), a)))

# def rif(a):
# 	if a[3]*a[2] < 100:
# 		print()
# 	return [a[0], round(val(a)+10)]
#
# def val(a):
# 	return a[3]*a[2]
#
# print(list(map(rif, a)))

