import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


L = [4,6,7,8,2,3,1,5,2]


def selection_sort(L):
  n = len(L)
  for c in range(n-1):
    m = L[c]
    index = c
    for i in range(c, n):
      if (L[i] < m):
        m = L[i]
        index = i 
    L.pop(index)
    L.insert(c, m)
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


make_animation(L, selection_sort)
print(L)