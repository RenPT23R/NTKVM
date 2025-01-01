import sys
import turtle as turt

def create_window():
    # Setup window
    window = turt.Screen()
    window.title("NTKVM - Launcher")
    window.bgcolor("white")
    window.setup(width=800, height=600)

    # Create a turtle for text
    pen = turt.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(-350, 0)
    pen.write("Please choose the file to open .exe or .scr file please\n>>> ", font=("Arial", 16, "normal"))

    return window, pen

def key_enter():
    # Capture user input
    path = window.textinput("File Selection", "Please choose the file to open .exe or .scr file please\n>>> ")

    # Clear the pen and display the result
    pen.clear()
    pen.goto(-350, -50)
    pen.write(f"You chose: {path}", font=("Arial", 16, "normal"))

    # Exit after displaying the choice
    window.bye()

# Initialize the window and pen
window, pen = create_window()

# Bind the Enter key
window.onkey(key_enter, "Return")
window.listen()
window.mainloop()