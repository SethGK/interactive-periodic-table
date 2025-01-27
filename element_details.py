import tkinter as tk
from tkinter import ttk
import json

def load_elements(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data["elements"]

def calculate_color_gradient(min_value, max_value, value):
    normalized_value = (value - min_value) / (max_value - min_value)
    red = int(normalized_value * 255)
    blue = int((1 - normalized_value) * 255)
    return f'#{red:02x}00{blue:02x}'

def add_electronegativity_gradient(elements):
    electronegativities = [
        element["electronegativity_pauling"]
        for element in elements
        if element["electronegativity_pauling"] is not None
    ]

    min_electronegativity = min(electronegativities)
    max_electronegativity = max(electronegativities)

    for element in elements:
        electronegativity = element.get("electronegativity_pauling")
        if electronegativity is not None:
            color = calculate_color_gradient(
                min_electronegativity, max_electronegativity, electronegativity
            )
        else:
            color = "#ffffff"  # Default to white if no electronegativity
        element["color"] = color



           

    