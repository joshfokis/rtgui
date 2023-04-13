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
    
def get_ticket(ticket_id):
    ticket = parse("rt.json")
    for t in ticket:
        if t['id'] == str(ticket_id):
            return t

def ticket_window(ticket_id):
    dicts = ["Queue", "Owner", "Creator", "Requestor", "LastUpdatedBy", "EffectiveId"]
    root = tk.Tk()
    root.title("RTQ")
    root.geometry("800x600")

    q_widget = ttk.Treeview(root)
    q_widget.pack(fill="both", expand=True)

    ticket = get_ticket(ticket_id)
    cf = parse("rt_customfields.json")
    for k,v in ticket.items():
        if k.startswith("_"):
            continue
        if not v:
            continue
        if k == "CustomFields":
            count = 0
            for f in cf:
               for c, vs in v.items():
                   if not vs:
                       continue
                   if f['id'] == c:
                       if count == c:
                           continue
                       ticket = q_widget.insert('', 0, text = f"{f['Name']}: {vs[0]}")
                       count = c

            continue
        if k in dicts:
            if not v:
                continue
            v = v['id']
        ticket = q_widget.insert('', 0, text = f"{k}: {v}")

    root.mainloop()

def search(text_input, dropdown_var, search_opts, prev_window):
    queues = parse("rtq.json")

    # Get the text from the text input widget
    text = text_input.get()

    # Get the value of the dropdown widget
    dropdown_value = dropdown_var.get()

    # Clear the text input widget
    text_input.delete(0, "end")

    # Clear the dropdown widget
    dropdown_var.set(search_opts[0])

    # Destroy the previous window
    prev_window.destroy()

    # Create a new tkinter window
    window = tk.Tk()

    # Create a listbox widget to display the search results
    listbox = tk.Listbox(window)
    listbox.pack(fill="both", expand=True)
    
    queue_id = 0

    if dropdown_value == "Queue":

        # Search the JSON data for the text input by the dropdown value
        for queue in queues:
            if text.lower() in queue["Name"].lower():
                if queue_id == queue['id']:
                    continue
                queue_id = queue['id']

        for ticket in parse("rt.json"):
            if queue_id in ticket["Queue"]["id"]:
                listbox.insert("end", f"ID: {ticket['id']} - {ticket['Subject']}")
    
    # Button to open ticket window with selected ticket
    open_ticket = tk.Button(window, text="Open Ticket", command=lambda:ticket_window(listbox.get(listbox.curselection()).split(" ")[1]))
    open_ticket.pack()

    # Start the tkinter main loop to display the window
    window.mainloop()

def search_window():
    
    search_opts = ["Queue", "Owner", "Requestor", "Id", "Subject", "Description"]

    # Create a new tkinter window
    window = tk.Tk()

    # Create a text input widget
    tk.Label(window, text="Search:").grid(row=0, column=0)
    text_input = tk.Entry(window)
    text_input.grid(row=0, column=1)

    # Create a dropdown widget and populate it with values from the JSON data
    tk.Label(window, text="Search by:").grid(row=1, column=0)

    # Set the default value of the dropdown to the first option
    dropdown_var = tk.StringVar(window)
    dropdown_var.set(search_opts[0])

    # Create the dropdown widget
    dropdown = tk.OptionMenu(window, dropdown_var, *search_opts)
    dropdown.grid(row=1, column=1)

    # Create a button to search the JSON data
    search_button = tk.Button(window, text="Search", command=lambda:search(text_input, dropdown_var, search_opts, window))
    search_button.grid(row=2, column=0)

    # Start the tkinter main loop to display the window
    window.mainloop()


def main():
    search_window()

def main_test():
    queues = parse("rtq.json")
    custom_fields = parse("rt_customfields.json")
    ticket = get_ticket(32)
    root = tk.Tk()
    root.title("RTQ")
    root.geometry("800x600")

     
    q_widget = ttk.Treeview(root)
    q_widget.pack(fill="both", expand=True)
    
    search_window()

    # queue_widget = tk.Listbox(root)
    # queue_widget.pack(fill="both", expand=True)
    
    #for t in ticket:
    #    ticket = q_widget.insert('', 0, text = f"ID: {t['id']}")
    #    q_widget.insert(ticket, "end", text = f"Name: {t['Subject']}")
    #    q_widget.insert(ticket, "end", text = f"Created: {t['Created']}")
    #    q_widget.insert(ticket, "end", text = f"Last Updated: {t['LastUpdated']}")


#    for queue in queues:
#        id = q_widget.insert('', 0, text = f"ID: {queue['id']}")
#        q_widget.insert(id, "end", text = f"Name: {queue['Name']}")
#        q_widget.insert(id, "end", text = f"Created: {queue['Created']}")
#        q_widget.insert(id, "end", text = f"Last Updated: {queue['LastUpdated']}")
        # q_widget.insert(id, "end", text = f"Name: {queue['Name']}")




    root.mainloop()

if __name__ == "__main__":
    main()
