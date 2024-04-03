def geometricSeries(a,r):
  x = a
  while True:
    yield x 
    x = x*r

s = geometricSeries(2,3)
for i in range(10):
  print(next(s))