# n=5  first row=0 i, space j=4 n-(i+1), star k = i+1

n=5
for i in range(n):
    space = "_"
    for j in range(n-(i+1)):
        space=j*space
    for k in range(i+1):
        star = k*"*"
    print(space,star)