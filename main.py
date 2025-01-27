import tkinter as tk
from tkinter import ttk
from table import create_periodic_table, load_elements, update_periodic_table_with_gradient


def main():
    elements = load_elements('data/elements.json')
    
    # Create the main window
    root = tk.Tk()
    root.title('Periodic Table')
    root.geometry('1290x750')  # Set the window size
    root.resizable(False, False)

    # Create a main frame to organize the layout
    main_frame = ttk.Frame(root)
    main_frame.pack(fill='both', expand=True)

    # Create the table frame for the periodic table
    table_frame = ttk.Frame(main_frame)
    table_frame.pack(side='top', fill='both', expand=True, padx=20, pady=20)

    # Create the periodic table in the table frame
    create_periodic_table(table_frame, elements)

    # Variable to track current state (True for gradient, False for default)
    is_gradient_view = tk.BooleanVar(value=False)

    # Function to toggle between views
    def toggle_view():
        if is_gradient_view.get():
            # Reset to default view
            create_periodic_table(table_frame, elements)
            toggle_button.config(text="Show Electronegativity Gradient")
            is_gradient_view.set(False)
        else:
            # Apply gradient view
            update_periodic_table_with_gradient(table_frame, elements)
            toggle_button.config(text="Reset to Default View")
            is_gradient_view.set(True)

    # Add the toggle button at the bottom of the main frame
    toggle_button = ttk.Button(
        main_frame,
        text="Show Electronegativity Gradient",
        command=toggle_view
    )
    toggle_button.pack(side='bottom', pady=10)

    # Start the main GUI loop
    root.mainloop()


if __name__ == '__main__':
    main()
