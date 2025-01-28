import json
import tkinter as tk
from tkinter import ttk
from element_details import *

def load_elements(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data["elements"]

def create_periodic_table_with_blocks(table_frame, elements):
    BLOCK_COLORS = {
    "s": "#ff9999",  # Light red for s-block
    "p": "#99ccff",  # Light blue for p-block
    "d": "#99ff99",  # Light green for d-block
    "f": "#ffcc99"   # Light orange for f-block
    }
    for widget in table_frame.winfo_children():
        widget.destroy()

    for element in elements:
        block = element.get("block", "s")
        color = BLOCK_COLORS.get(block, "#ffffff") 
        text_color = get_contrasting_text_color(color)

        style_name = f"{element['symbol']}.TButton"
        style = ttk.Style()
        style.configure(
            style_name,
            background=color,
            foreground=text_color,
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

def add_legend(frame):
    BLOCK_COLORS = {
    "s": "#ff9999",  # Light red for s-block
    "p": "#99ccff",  # Light blue for p-block
    "d": "#99ff99",  # Light green for d-block
    "f": "#ffcc99"   # Light orange for f-block
    }
    for block, color in BLOCK_COLORS.items():
        label = ttk.Label(frame, text=f"{block}-block", background=color, width=10, anchor="center")
        label.pack(side="left", padx=5, pady=5)


def update_periodic_table_with_gradient(table_frame, elements, trend="electronegativity"):
    if trend == "electronegativity":
        add_electronegativity_gradient(elements)
    elif trend == "electron_affinity":
        add_electron_affinity_gradient(elements)

    for button, element in zip(table_frame.winfo_children(), elements):
        color = element.get("color", "#ffffff")
        text_color = get_contrasting_text_color(color)

        style_name = f"{element['symbol']}.TButton"
        style = ttk.Style()
        style.configure(
            style_name,
            background=color,
            foreground=text_color,
            relief="flat",
            width=6,
            anchor="center",
            padding=2,
        )

        button.configure(style=style_name)


def update_periodic_table_with_ionization_energy(table_frame, elements):
    add_ionization_energy_gradient(elements)

    for widget in table_frame.winfo_children():
        widget.destroy()

    ionization_energies = [
        element["ionization_energies"][0] if "ionization_energies" in element and element["ionization_energies"] else None
        for element in elements
    ]
    ionization_energies = [e for e in ionization_energies if e is not None]
    min_ionization = min(ionization_energies)
    max_ionization = max(ionization_energies)

    for element in elements:
        ionization_energy = element["ionization_energies"][0] if "ionization_energies" in element and element["ionization_energies"] else None
        color = (
            calculate_color_gradient(min_ionization, max_ionization, ionization_energy)
            if ionization_energy is not None
            else "#ffffff"
        )
        text_color = get_contrasting_text_color(color)

        style_name = f"{element['symbol']}_ionization.TButton"
        style = ttk.Style()
        style.configure(
            style_name,
            background=color,
            foreground=text_color,
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
    details_window.geometry('400x500')


    frame = ttk.Frame(details_window)
    frame.pack(fill='both', expand=True, padx=10, pady=10)

    canvas = tk.Canvas(frame)
    canvas.pack(side='left', fill='both', expand=True)

    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=canvas.yview)
    scrollbar.pack(side='right', fill='y')

    inner_frame = ttk.Frame(canvas)

    inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')

    canvas.configure(yscrollcommand=scrollbar.set)

    basic_info = [
        f"Symbol: {element['symbol']}",
        f"Name: {element['name']}",
        f"Atomic Number: {element['number']}",
        f"Category: {element['category']}",
        f"Phase: {element['phase']}",
        f"Atomic Mass: {element['atomic_mass']}",
        f"Density: {element.get('density', 'Unknown')} g/cm³",
        f"Molar Heat: {element.get('molar_heat', 'Unknown')} J/(mol·K)",
        f"Discovered By: {element.get('discovered_by', 'Unknown')}",
    ]
    for info in basic_info:
        label = ttk.Label(inner_frame, text=info, wraplength=350, justify='left', font=('Arial', 10))
        label.pack(anchor='w', pady=2)

    ttk.Label(inner_frame, text="Electron Configuration:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=5)
    ttk.Label(inner_frame, text=element['electron_configuration'], wraplength=350, justify='left').pack(anchor='w')

    if 'electron_affinity' in element:
        ttk.Label(inner_frame, text=f"Electron Affinity: {element['electron_affinity']} kJ/mol").pack(anchor='w')

    if 'electronegativity_pauling' in element:
        ttk.Label(inner_frame, text=f"Electronegativity (Pauling): {element['electronegativity_pauling']}").pack(anchor='w')

    if 'melt' in element and 'boil' in element:
        ttk.Label(inner_frame, text=f"Melting Point: {element['melt']} K").pack(anchor='w')
        ttk.Label(inner_frame, text=f"Boiling Point: {element['boil']} K").pack(anchor='w')


    ttk.Label(inner_frame, text="Summary:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=5)
    ttk.Label(inner_frame, text=element['summary'], wraplength=350, justify='left').pack(anchor='w')




    

