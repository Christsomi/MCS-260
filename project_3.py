import random
import matplotlib.pyplot as plt 


#PUT COMMENTS (!!!!)

def F(L, t, n):
  Px = []
  Py = []

  for point in L:
      Px.append(point[0])
      Py.append(point[1])

  current_position = t
  
  for _ in range(n):

    random_number = random.randint(1, 6)
    if random_number == 1 or random_number == 2:
      point = [0,0]
    elif random_number == 3 or random_number == 4:
      point = [10, 0]
    else:
      point = [5, 10]

    current_position = ((current_position[0] + point[0]) / 2, (current_position[1] + point[1]) / 2)
          
    Px.append(current_position[0])
    Py.append(current_position[1])

  plt.scatter(Px, Py)
    
  plt.xlabel("X")
  plt.ylabel("Y")
  plt.title("Fractal Plot")
    
  plt.show()

F([(0,0),(10,0),(5,10)], (2,3), 10000)