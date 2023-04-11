import bson
import json
import tkinter as tk
from tkinter import ttk

def parse(file):
    objs = []    
    if not file:
        return
    with open(file, "rb") as f:
        data = json.load(f)
        for obj in data:
            yield obj

def create_fields():
    pass

def example_main():
   # Create a new tkinter window
    window = tk.Tk()

    # Create a section for personal information
    personal_info_frame = tk.Frame(window)
    personal_info_frame.pack(fill="both", expand=True)
    
    for k,v in a.items():
        tk.Label(personal_info_frame, text=k)
        tk.Entry(personal_info_frame, text=v)
    # Start the main event loop to display the window
    window.mainloop()

def main():
    queues = parse("rtq.json")
    custom_fields = parse("rt_customfields.json")

    root = tk.Tk()
    root.title("RTQ")
    root.geometry("800x600")

    
    q_widget = ttk.Treeview(root)
    q_widget.pack(fill="both", expand=True)

    # queue_widget = tk.Listbox(root)
    # queue_widget.pack(fill="both", expand=True)

    for queue in queues:
        id = q_widget.insert('', 0, text = f"ID: {queue['id']}")
        q_widget.insert(id, "end", text = f"Name: {queue['Name']}")
        q_widget.insert(id, "end", text = f"Created: {queue['Created']}")
        q_widget.insert(id, "end", text = f"Last Updated: {queue['LastUpdated']}")
        # q_widget.insert(id, "end", text = f"Name: {queue['Name']}")




    root.mainloop()

if __name__ == "__main__":
    main()
