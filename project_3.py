import random
import matplotlib.pyplot as plt 


def F(L, t, n):
  #0. Initialize two empty lists Px and Py, which will store x and y coordinates of points.
  Px = [] 
  Py = []

  for point in L: #1. Takes a list of three points (coordinate points (x,y)) in a plane to form a corners of a triangle, i.e. [(0,0),(10,0),(5,10)] and places them into Px and Py
      Px.append(point[0])
      Py.append(point[1])
  
  #print(Px, Py)

  current_position = t #2. Point (2,3) inside the triangle is an initial point and a current position.
  
  for x in range(n): #6. Repeat from step 3 a 10000 times

    random_number = random.randint(1, 6) #3. Simulating an ordinary six-sided dice
    if random_number == 1 or random_number == 2:
      point = [0,0]
    elif random_number == 3 or random_number == 4:
      point = [10, 0]
    else:
      point = [5, 10]

    current_position = ((current_position[0] + point[0]) / 2, (current_position[1] + point[1]) / 2) #4. Move half the distance from the current position to the selected point

    #5. Store the points
    Px.append(current_position[0])
    Py.append(current_position[1])

#7. Create a scatter plot of the points
  plt.scatter(Px, Py)

#8.
  plt.xlabel("X")
  plt.ylabel("Y")
  plt.title("Fractal Plot")
#9.
  plt.show()
#10.
F([(0,0),(10,0),(5,10)], (2,3), 10000)