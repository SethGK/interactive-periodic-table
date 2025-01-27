import tkinter as tk
from tkinter import ttk
from table import create_periodic_table, load_elements

def main():
    elements = load_elements('data/elements.json')
    root = tk.Tk()
    root.title('Periodic Table')
    root.geometry('1120x600')
    root.resizable(False, False)

    create_periodic_table(root, elements)

    root.mainloop()

if __name__ == '__main__':
    main()    
    





    
