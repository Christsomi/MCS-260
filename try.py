import random
import matplotlib.pyplot as plt

def F(L, t, n):
    # Initialize two empty lists to store x and y coordinates
    Px = []
    Py = []
    
    # Step 1: Populate Px and Py with initial triangle vertices
    Px.extend([point[0] for point in L])
    Py.extend([point[1] for point in L])
    
    # Step 2: Set initial position
    current_position = t
    
    # Step 3-6: Perform random walk for n iterations
    for _ in range(n):
        # Step 3: Randomly select one of the three points
        roll = random.randint(1, 6)
        if roll in (1, 2):
            selected_point = L[0]
        elif roll in (3, 4):
            selected_point = L[1]
        else:
            selected_point = L[2]
        
        # Step 4: Move half the distance to the selected point
        current_position = ((current_position[0] + selected_point[0]) / 2, 
                            (current_position[1] + selected_point[1]) / 2)
        
        # Step 5: Store current position
        Px.append(current_position[0])
        Py.append(current_position[1])
    
    # Step 7: Create scatter plot
    plt.scatter(Px, Py)
    
    # Step 8: Add labels and title
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Fractal Plot")
    
    # Step 9: Display plot
    plt.show()

# Step 10: Call the function
F([(0,0),(10,0),(5,10)], (2,3), 10000)
