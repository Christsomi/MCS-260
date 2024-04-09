import random

L = [random.randint(1,100) for x in range(30)]
L.sort()
print(L)

def binarysearch(L, x):
  'A function that does a binary search of a sorted list using recursion.'

  if (len(L) == 0):
    return False
  half = len(L)//2
  if (x<L[half]):
    return binarysearch(L[0:half], x)
  elif(x>L[half]):
    return binarysearch(L[half+1:len(L)], x)
  else:
    return True
  
print(binarysearch(L,37))