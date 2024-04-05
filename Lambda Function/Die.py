import random

die = lambda : print(random.randint(1,6))

def twice(f):
  'performs the function f() twice'
  f()
  f()

twice(die)

#Or:

die2 = lambda : random.randint(1,6)
twice(lambda: print(die2()))