import itertools
inp = input("Enter a set of numbers: ")
lst = list(inp)
combs = []

for i in range(0, len(lst)+1):
    els = [list(x) for x in itertools.combinations(lst, i)]
    combs.append(els)
print(combs)

