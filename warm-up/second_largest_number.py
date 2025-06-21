arr = [2,5,1,-1,-1,3,0,10,6,-2,13,13,13,-3]
# arr=[-1,0]
def second_largest(array):
    largest=float('-inf')
    second_largest=largest-1
    for element in arr:
        if element>largest and element!=largest:
            temp=largest
            largest=element
            second_largest=temp
    return largest,second_largest

print(second_largest(arr))