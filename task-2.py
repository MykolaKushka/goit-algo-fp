import matplotlib.pyplot as plt
import numpy as np

def draw_pythagoras_tree(ax, x, y, angle, size, level):
    if level == 0:
        return
    
    # Calculate the points of the square
    x1 = x + size * np.cos(np.radians(angle))
    y1 = y + size * np.sin(np.radians(angle))
    x2 = x1 - size * np.sin(np.radians(angle))
    y2 = y1 + size * np.cos(np.radians(angle))
    x3 = x - size * np.sin(np.radians(angle))
    y3 = y + size * np.cos(np.radians(angle))
    
    # Draw the square
    ax.plot([x, x1], [y, y1], 'r-')
    ax.plot([x1, x2], [y1, y2], 'r-')
    ax.plot([x2, x3], [y2, y3], 'r-')
    ax.plot([x3, x], [y3, y], 'r-')
    
    # Calculate the new sizes and angles
    new_size = size / np.sqrt(2)
    new_angle1 = angle + 45
    new_angle2 = angle - 45
    
    # Draw the two smaller trees
    draw_pythagoras_tree(ax, x3, y3, new_angle1, new_size, level - 1)
    draw_pythagoras_tree(ax, x2, y2, new_angle2, new_size, level - 1)

def main():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    recursion_level = int(input("Enter recursion level (1-10): "))
    draw_pythagoras_tree(ax, 0, 0, 90, 1, recursion_level)
    
    plt.show()

if __name__ == "__main__":
    main()
