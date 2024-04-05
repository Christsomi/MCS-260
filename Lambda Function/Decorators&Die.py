import random

die = lambda : random.randint(1,6)

def twice(f):
  'performs the function f() twice'
  f()
  f()

@twice #Easy creation of higher order functions
def print_die():
  print(die())
