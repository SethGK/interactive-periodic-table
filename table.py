import json
import tkinter as tk
from tkinter import ttk
from element_details import add_electronegativity_gradient

def load_elements(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data["elements"]

def create_periodic_table(table_frame, elements):
    default_style = ttk.Style()
    default_style.configure(
        "Default.TButton",
        background="#ffffff",
        relief="flat",
        width=6,
        anchor="center",
        padding=2,
    )

    for element in elements:
        button = ttk.Button(
            table_frame,
            text=f"{element['symbol']}\n{element['number']}\n{element['atomic_mass']:.2f}",
            style="Default.TButton",
            command=lambda e=element: show_element_details(e),
        )
        button.grid(row=element['ypos'], column=element['xpos'] - 1, padx=2, pady=2)


def update_periodic_table_with_gradient(table_frame, elements):
    add_electronegativity_gradient(elements)

    for button, element in zip(table_frame.winfo_children(), elements):
        color = element.get("color", "#ffffff")
        style_name = f"{element['symbol']}.TButton"

        style = ttk.Style()
        style.configure(style_name, background=color, relief="flat")

        
        button.configure(style=style_name)


    for widget in table_frame.winfo_children():
        widget.destroy() 

    for element in elements:
        electronegativity = element.get('electronegativity_pauling')
        color = element.get('color', "#ffffff") 

        style_name = f"{element['symbol']}.TButton"
        style = ttk.Style()
        style.configure(
            style_name,
            background=color,
            relief="flat",
            width=6,
            anchor="center",
            padding=2,
        )

        button = ttk.Button(
            table_frame,
            text=f"{element['symbol']}\n{element['number']}\n{element['atomic_mass']:.2f}",
            style=style_name,
            command=lambda e=element: show_element_details(e),
        )
        button.grid(row=element['ypos'], column=element['xpos'] - 1, padx=2, pady=2)


def show_element_details(element):
    details_window = tk.Toplevel()
    details_window.title(element['name'])
    details_window.geometry('400x300')

    symbol_label = ttk.Label(details_window, text=f"Symbol: {element['symbol']}")
    symbol_label.pack(pady=10)

    name_label = ttk.Label(details_window, text=f"Name: {element['name']}")
    name_label.pack(pady=10)

    atomic_mass_label = ttk.Label(details_window, text=f"Atomic Mass: {element['atomic_mass']}")
    atomic_mass_label.pack(pady=10)

    discovered_by_label = ttk.Label(details_window, text=f"Discovered By: {element['discovered_by']}")
    discovered_by_label.pack(pady=10)

    frame = ttk.Frame(details_window)
    frame.pack(fill='both', expand=True, padx=10, pady=5)

    canvas = tk.Canvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=canvas.yview)
    inner_frame = ttk.Frame(canvas)

    inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    canvas.create_window((0, 0), window=inner_frame, anchor='nw')
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')
    
    summary_label = ttk.Label(inner_frame, text=element['summary'], wraplength=350, justify='left', font=('Arial', 10))
    summary_label.pack(anchor='w', padx = 5)
    

