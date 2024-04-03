class NaturalNumber:
  def __inter__(self):
    self.n = 0
    return self
  def __next__(self):
    x = self.n
    self.n = x+1
    return x
  
class Range:
  def __init__(self,start,stop, step = 1):
    self.start = start
    self.stop = stop
    self.step = step
  def __getitem__(self, i):
    x = self.start + i*self.step
    if x>=self.stop:
      raise IndexError
    return x

def count():
  x=0
  while True:
    yield x
    x +=1

def example2():
  L = [1,2,3,4,5,6]
  I = iter(L)
  while True:
    try:
      x = next(I)
      print(x)
    except StopIteration:
      break

def example3():
  r = Range(2,5)
  print(r[2])
  for x in r:
    print(x)

def example4():
  it = count()
  for i in range(10):
    print(next(it))

example4()