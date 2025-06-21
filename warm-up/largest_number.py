# arr = [2,5,1,-1,-1,3,0,10,6,-2,11,13,-3]
arr = [-2]

def largest_number(array):
    max = float('-inf')
    for element in arr:
        if element>max:
            max=element
    return max

print(largest_number(arr))