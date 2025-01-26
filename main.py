import tkinter as tk
from tkinter import ttk

def create_main_window():
    root = tk.Tk()
    root.title('Periodic Table')
    root.geometry('800x600')
    root.resizable(False, False)

    title_label = ttk.Label(root, text='Periodic Table', font=('Arial', 20, 'bold'))
    title_label.pack(pady=10)

    table_frame = ttk.Frame(root)
    table_frame.pack(fill='both', expand=True, padx=20, pady=20)

    place_holder_label = ttk.Label(table_frame, text='Table goes here', font=('Arial', 16))
    place_holder_label.pack(expand=True)

    root.mainloop()

if __name__ == '__main__':
    create_main_window()    
    





    
