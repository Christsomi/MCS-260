import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


L = [random.randint(0,100) for x in range(20)]

def insertion_sort(L):
  n = len(L)
  for c in range(n-1):
    x = L[c]
    index = c
    for i in range(c):
      if L[i] > x:
        index = i
        break
    L.pop(c)
    L.insert(index, x)
    yield

def make_animation(L,sort,delay = 100):
    fig = plt.figure()
    global bar
    bar = plt.bar(range(len(L)), L)
    it = sort(L)
    anim = animation.FuncAnimation(fig,animate,repeat = False,blit = False,frames = it,interval=delay )
    plt.show()

def animate(i):
    for j,b in enumerate(bar):
        b.set_height(L[j])


make_animation(L, insertion_sort)
print(L)

