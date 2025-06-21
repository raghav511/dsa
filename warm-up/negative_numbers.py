# write a function that returns the number of negartive
# numbers in an array

arr = [2,5,1,-1,-1,3,0,10,6,-2,11,13,-3]

def negative_count(array):
    negative_num = []
    for element in array:
        if element <0 and element not in negative_num:
            negative_num.append(element)
    return negative_num

print(negative_count(arr))