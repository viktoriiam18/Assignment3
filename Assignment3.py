# Program Name: Assignment3.py
# Course: IT3883 / Section: fW01 (85546)
# Student Name: Viktoriia Morozova
# Assignment Number: 3
# Due Date: 10/10/2026
# Purpose: Convert miles per gallon to kilometers per liter in a GUI.
# The result updates as the user types. Blank and invalid input are handled.
# Resources: Assignment 3 instructions; Module 3-2 GUI presentation.


import math
import tkinter as tk
from tkinter import ttk

MPG_TO_KM_PER_LITER = 0.425143707


def format_conversion(text):
    """Return a result or a helpful message for the current input."""
    cleaned_text = text.strip()
    if not cleaned_text:
        return "Enter an MPG value above."
    try:
        miles_per_gallon = float(cleaned_text)
    except ValueError:
        return "Please enter a valid number."
    if not math.isfinite(miles_per_gallon):
        return "Please enter a finite number."
    if miles_per_gallon < 0:
        return "MPG cannot be negative."
    kilometers_per_liter = miles_per_gallon * MPG_TO_KM_PER_LITER
    return f"{kilometers_per_liter:.4f} km/L"


def main():
    # Create the main window and a container with comfortable spacing.
    window = tk.Tk()
    window.title("Fuel Economy Converter")
    window.resizable(False, False)
    content = ttk.Frame(window, padding=24)
    content.grid(row=0, column=0)

    # Tkinter variables connect the input and output to their widgets.
    mpg_input = tk.StringVar(master=window)
    conversion_output = tk.StringVar(master=window)

    ttk.Label(content, text="MPG to Kilometers per Liter",
              font=("Arial", 16, "bold")).grid(row=0, column=0, pady=(0, 20))
    ttk.Label(content, text="Miles per Gallon (MPG)").grid(
        row=1, column=0, sticky="w")
    input_field = ttk.Entry(content, textvariable=mpg_input, width=35)
    input_field.grid(row=2, column=0, sticky="ew", pady=(6, 18))
    ttk.Label(content, text="Kilometers per Liter (km/L)").grid(
        row=3, column=0, sticky="w")
    ttk.Label(content, textvariable=conversion_output,
              font=("Arial", 12), wraplength=320).grid(
        row=4, column=0, sticky="w", pady=(6, 0))

    # A write trace also detects deletion and pasted text, without a button.
    def update_result(*args):
        conversion_output.set(format_conversion(mpg_input.get()))

    mpg_input.trace_add("write", update_result)
    update_result()
    input_field.focus_set()
    window.mainloop()


# Importing this file does not open a window; running it directly does.
if __name__ == "__main__":
    main()
