"""
Exercise 3.3
Draw a grid using functions
Author: Tran Ngoc Hieu
MSSV: 25112045
"""

# Function to draw a horizontal line
def print_horizontal():
    print("+ - - - - + - - - - +")

# Function to draw a vertical line
def print_vertical():
    print("|         |         |")

# Function to draw a 2x2 grid
def draw_grid():
    print_horizontal()
    for i in range(4):
        print_vertical()
    print_horizontal()
    for i in range(4):
        print_vertical()
    print_horizontal()

# Run the function
draw_grid()