def threshold(sum):
    if sum >= 1:
        return 1
    else:
        return 0

def XOR(input1, input2):
    weight1 = 1
    weight2 = 1
    threshold_value = 1
    
    sum = input1 * weight1 + input2 * weight2
    
    output = threshold(sum - threshold_value)
    
    return output

print(XOR(0, 0)) 
print(XOR(0, 1))
print(XOR(1, 0))
print(XOR(1, 1))
