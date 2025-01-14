import turtle  # Import the turtle graphics module

print("Example")
print("Enter left branch angle (in degrees): 20")
print("Enter right branch angle (in degrees): 25")
print("Enter starting branch length: 100")
print("Enter recursion depth: 5")
print("Enter branch length reduction factor (e.g., 0.7): 0.7")

print("")
print("")
print("")
print("----------------------------------------------------------------")
print("")

# Function to draw the tree branches recursively
def draw_branch(t, branch_length, left_angle, right_angle, depth, reduction_factor):
    """
    Draws a recursive tree with green leaves using Turtle graphics.

    Parameters:
    t (Turtle): The turtle object used for drawing.
    branch_length (float): Length of the current branch.
    left_angle (float): Angle to turn left for the left branch.
    right_angle (float): Angle to turn right for the right branch.
    depth (int): Remaining depth of recursion.
    reduction_factor (float): Factor to reduce branch length with each level.
    """
    
    if depth == 0:
        # Base case: if recursion depth reaches 0, draw a green leaf
        t.pencolor("green")  # Set pen color to green for leaves
        t.dot(branch_length * 0.5)  # Draw a small circle as a leaf
        return  # End the recursive call for this branch

    # Set the pen thickness based on the depth for visual effect
    t.pensize(depth * 2)  # Thicker branches for higher levels
    # Set the pen color to a brownish shade, which lightens as depth decreases
    t.pencolor((0.5 + 0.5 * depth / 10, 0.25, 0.1))  # RGB values for a brown color

    # Draw the main branch
    t.forward(branch_length)

    # Draw the left branch
    t.left(left_angle)  # Turn the turtle to the left by the specified angle
    draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)

    # Return to the main branch base after drawing the left branch
    t.right(left_angle + right_angle)  # Turn right to prepare for the right branch
    draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)

    # Reset the turtle's direction to the original state
    t.left(right_angle)  # Turn back left to the original orientation
    t.backward(branch_length)  # Move back to the starting position of the branch

# Main function to set up the turtle environment and start drawing
def main():
    try:
        # Prompt the user for tree parameters
        left_angle = float(input("Enter left branch angle (in degrees): "))  # Left branch angle
        right_angle = float(input("Enter right branch angle (in degrees): "))  # Right branch angle
        branch_length = float(input("Enter starting branch length: "))  # Initial branch length
        depth = int(input("Enter recursion depth: "))  # Number of levels for recursion
        reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7): "))  # Reduction factor

        # Set up the turtle screen
        screen = turtle.Screen()  # Create the screen
        screen.setup(width=800, height=600)  # Set the screen size
        screen.title("Recursive Tree with Green Leaves")  # Title of the Turtle window

        # Set up the turtle object
        t = turtle.Turtle()  # Create the turtle
        t.speed("fastest")  # Set the turtle speed to the fastest
        t.left(90)  # Point the turtle upwards (default starts to the right)
        t.penup()  # Lift the pen so it doesn't draw while moving
        t.goto(0, -250)  # Move the turtle to the bottom center of the screen
        t.pendown()  # Lower the pen to start drawing

        # Start drawing the recursive tree
        draw_branch(t, branch_length, left_angle, right_angle, depth, reduction_factor)

        # Keep the turtle graphics window open until manually closed
        screen.mainloop()

    except turtle.Terminator:
        # Handle the case when the Turtle graphics window is closed
        print("Turtle graphics program was terminated.")
    finally:
        try:
            # Ensure proper cleanup of the Turtle graphics window
            turtle.bye()
        except turtle.Terminator:
            pass  # Ignore if the screen is already closed

# Entry point of the program
if __name__ == "__main__":
    main()  # Run the main function
