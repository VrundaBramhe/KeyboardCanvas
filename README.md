# KeyboardCanvas

## Overview
KeyboardCanvas is an interactive Python project that utilizes the Turtle graphics module to create drawings controlled by keyboard inputs. With KeyboardCanvas, users can guide a virtual turtle across the canvas, using arrow keys for movement and other keys for additional actions, such as clearing the screen.

## Features
- **Directional Movement:**
  - **Up Arrow Key:** Moves the turtle brush forward.
  - **Down Arrow Key:** Moves the turtle brush backward.
  - **Left Arrow Key:** Rotates the turtle brush counterclockwise.
  - **Right Arrow Key:** Rotates the turtle brush clockwise.
- **Screen Clearing:**
  - **'C' Key:** Clears the entire drawing canvas when pressed twice in quick succession (double-clicked).

## Getting Started
1. Ensure Python is installed on your system.
2. Install the Turtle module if not already included.
3. Download the KeyboardCanvas project files.
4. Execute the Python script to launch the application.
5. Use the arrow keys for directional movement and 'C' key for screen clearing.

## Example Code Snippet
```python
import turtle

# Function definitions for movement and screen clearing
def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def turn_left():
    turtle.left(15)

def turn_right():
    turtle.right(15)

def clear_screen():
    turtle.clear()

# Set up screen and key bindings
screen = turtle.Screen()
screen.title("KeyboardCanvas")
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
scr

