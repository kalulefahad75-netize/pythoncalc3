Python Tkinter Calculator

A clean, desktop-based calculator application built with Python using the Tkinter library. It features a modern "Cadet Blue" theme and provides all the essential arithmetic functions.

Key Features

Basic Arithmetic: Addition, Subtraction, Multiplication, and Division.

Smart Editing: Includes Backspace (←), Clear Entry (CE), and All Clear (C) functionality.

Advanced Toggle: A ± button to instantly switch between positive and negative values.

How to Use

Input: Click the buttons to build your mathematical expression.
Calculate: Press = to see the result.
Correction: Use the ← button to fix mistakes or C to start over.
Negative Numbers: Press ± to invert the current number on the display.

===Code Structure===

__init__: Sets up the main window, frames, and color styling.

create_button: A reusable method to generate UI buttons efficiently.

button_click: The "brain" of the app that processes input and calculates results using Python's eval() function.
