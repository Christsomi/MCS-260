#Divide the list up into two parts
#Sort each half of the data using merge sort 
#Merge two sorted halves back together

L = [2,7,3,5,8,1,4,6]
0

#DOES NOT WORK
def merge_sort(L,a,b): #a = left end #b = right end
  half = (a+b) //2
  merge_sort(L,a,half)
  merge_sort(a,half+1,b)

  L1 = L[a:half+1]
  L2 = L[half+1:b+1]

  i = a
  while True:
    if(L1[0] <= L2[0]):
      x = L1.pop(0)
    else:
      x = L2.pop(0)
    L[i] = x
    i+=1

merge_sort(L, 0, len(L)-2)
print(L)