import tkinter as tk
from tkinter import ttk
from element_details import *
from table import *

def main():
    elements = load_elements('data/elements.json')

    root = tk.Tk()
    root.title('Periodic Table')
    root.resizable(True, True)

    main_frame = ttk.Frame(root)
    main_frame.pack(fill='both', expand=True)

    table_frame = ttk.Frame(main_frame)
    table_frame.pack(side='top', fill='both', expand=True, padx=20, pady=20)

    create_periodic_table(table_frame, elements)

    selected_trend = tk.StringVar(value="default")

    def apply_gradient():
        trend = selected_trend.get()
        if trend == "default":
            create_periodic_table(table_frame, elements)
        elif trend == "ionization_energy":
            update_periodic_table_with_ionization_energy(table_frame, elements)
        else:
            update_periodic_table_with_gradient(table_frame, elements, trend)

    trend_menu = ttk.OptionMenu(
        main_frame,
        selected_trend,
        "default",
        "default",
        "electronegativity",
        "electron_affinity",
        "ionization_energy",
    )
    trend_menu.pack(side='left', padx=10, pady=10)

    apply_button = ttk.Button(
        main_frame,
        text="Apply Gradient",
        command=apply_gradient
    )
    apply_button.pack(side='left', padx=10, pady=10)

    root.update_idletasks()
    width = table_frame.winfo_reqwidth() + 50
    height = table_frame.winfo_reqheight() + 150 
    root.geometry(f"{width}x{height}")

    root.mainloop()



if __name__ == '__main__':
    main()
