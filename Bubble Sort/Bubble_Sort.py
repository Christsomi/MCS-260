import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L = [2,7,3,5,8,1]
# [2,7,3,5,8,1] - compares 2 and 7
# compares 3 and 7 - swaps
# [2,3,7,5,8,1] - compares 7 and 5
# swaps
# [2,3,5,7,8,1] - conpare 8 and 1 continue until 1 is before 2
# [1,2,3,5,7,8]

M = [random.randint(0,100) for x in range(20)]

def bubble_sort(M):
    n = len(M)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if M[j] > M[j + 1]:
                M[j], M[j + 1] = M[j + 1], M[j]
            yield
bubble_sort(M)
print(M)

def make_animation(M,sort,delay = 100):
    fig = plt.figure()
    global bar
    bar = plt.bar(range(len(M)), M)
    it = sort(M)
    anim = animation.FuncAnimation(fig,animate,repeat = False,blit = False,frames = it,interval=delay )
    plt.show()

def animate(i):
    for j,b in enumerate(bar):
        b.set_height(M[j])

make_animation(M, bubble_sort)
print(M)