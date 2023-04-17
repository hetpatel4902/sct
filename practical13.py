A = {(0,0):0.2, (0,1):0.5, (1,0):0.8, (1,1):0.4}
B = {(0,0):0.6, (0,1):0.3, (1,0):0.7, (1,1):0.1}

def max_min_composition(A, B):
    C = {}
    for x in A.keys():
        for y in B.keys():
            z = (x[1], y[0])
            if z not in C.keys():
                C[z] = min(A[x], B[y])
            else:
                C[z] = max(C[z], min(A[x], B[y]))
    return C

C = max_min_composition(A, B)

print(C)
