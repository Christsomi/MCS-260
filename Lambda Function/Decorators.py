def h(func): #Takes in a function and gives back another function
  def eval():
    v = func()
    return v+2 #(3+2)
  return eval

def g(func):
  def eval():
    x = func()
    return x*x #(3+2)^2
  return eval

@g
@h
def f():
  return 3 #(3+2)^2 = 25

print(f())


