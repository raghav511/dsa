arr = [2,5,1,3,0,10,6,11,13]
import datetime
def find_num(ele,arr):
    # brute force
    start = datetime.datetime.now()
    for element in arr:
        if ele==element:
            end = datetime.datetime.now()
            total_time = end - start
            print(f'Time taken: {total_time}')
            return True
    end = datetime.datetime.now()
    total_time = end - start
    print(f'Time taken: {total_time}')
    return False
    # sort and do binary search
    '''
    start = datetime.datetime.now()
    arr.sort()
    left = 0
    right = len(arr)-1
    while left<=right:
        mid=int((left+right)/2)
        if arr[mid]==ele:
            end = datetime.datetime.now()
            total_time = end - start
            print(f'Time taken: {total_time}')
            return True
        elif arr[mid]<ele:
            left=mid+1
        else:
            right=mid-1
    end = datetime.datetime.now()
    total_time = end - start
    print(f'Time taken: {total_time}')
    return False
'''
print(find_num(10,arr))