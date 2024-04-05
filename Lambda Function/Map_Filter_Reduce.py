#MAP
#Gives a new iterable applying the function to each one
L = [2,3, 'red', 'blue']
M = list(map(lambda x:2*x, L))
print(M)

I = [2,3,-1,-5,-6,7,8]
K = list(map(abs,I))
print(K)

K = list(map(lambda x: x**2,I))
print(K)

#FILTER
#Applies the criteria to each element of the sequence keeping only those that are True giving a map object
D = list(filter(lambda x: x>0, I))
print(D)


#REDUCE
#Applies the function successively first to the first two elements
import functools as ft
total = ft.reduce(lambda x,y: x+y, [-2,3,-4,6])
print(total)