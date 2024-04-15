import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


L = [random.randint(0,100) for x in range(20)]

def insertion_sort(L):
    n = len(L) 
      
    if n <= 1:
        return  
 
    for i in range(1, n): 
        key = L[i] 
        j = i-1
        while j >= 0 and key < L[j]:  
            L[j+1] = L[j] 
            j -= 1
        L[j+1] = key
    yield

def insertion_sort_two(L):
    n = len(L)
    for c in range(n):
        x = L[c]
        index = c
        a = 0
        b = 0
        while True:
            half = (b+a)//2
            if (b-a <= 1):
                if(x <= L[a]):
                    index = a
                    break
                elif (x>=L[b]):
                    index = b
                    break
                else:
                    index = half
                    break
            if(L[half] == x):
                index = half
                break
            elif(x < L[half]):
                b = half
            else:
                a= half
        pop_and_insert(L, c, index)
        yield

def pop_and_insert(L, c, index): #c > index
    #temp = L[index]
    #L[index] = L[c] 
        
    #temp2 = L[index + 1]
    #L[index + 1] = temp
    #temp = L[index+1]
    #L[index + 2] = temp2

    #L[c] = temp

    temp = L[index]
    L[index] = L[c]
    for i in range(index, c):
        temp2 = L[1 +1]
        L [i + 1] = temp
        temp = temp2

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

