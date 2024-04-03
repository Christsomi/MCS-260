import itertools

s = 'abc'
hello = "hello"

it = itertools.cycle(s)
it2 = itertools.repeat(s)
it3 = itertools.combinations(hello, 3)

for x in it3:
  print(x)

for x in range(100):
  print(next(it))
  print(next(it2))

