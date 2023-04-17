def is_equivalence_relation(R):
    for x in set([pair[0] for pair in R.keys()]):
        if R.get((x, x), 0) != 1:
            return False

    for pair, degree in R.items():
        if pair[0] != pair[1] and R.get((pair[1], pair[0]), 0) != degree:
            return False

    for x, y, z in [(pair1[0], pair2[0], pair2[1]) for pair1 in R.keys() for pair2 in R.keys() if pair1[1] == pair2[0]]:
        r1 = R.get((x, y), 0)
        r2 = R.get((y, z), 0)
        if r1 != 0 and r2 != 0 and R.get((x, z), 0) != min(r1, r2):
            return False

    return True
R = {('a', 'a'): 1, ('b', 'b'): 1, ('c', 'c'): 1, ('a', 'b'): 0.5, ('b', 'a'): 0.5, ('b', 'c'): 0.7, ('c', 'b'): 0.7, ('a', 'c'): 0.3, ('c', 'a'): 0.3}

if is_equivalence_relation(R):
    print("The given fuzzy relation is an equivalence relation.")
else:
    print("The given fuzzy relation is not an equivalence relation.")
