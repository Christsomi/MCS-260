import time

def fact1(n):
  'has max recursion depth'
  if(n ==0 or n==1):
    return 1
  else:
    return n*fact1(n-1) 

def fact2(n):
  prod = 1
  for i in range(1,n+1):
    prod = prod*i  
  return prod

start = time.time()
fact2(5)
end = time.time()
print(end-start)

start = time.time()
fact1(5)
end = time.time()
print(end-start)


