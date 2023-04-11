import bson
import json
import tkinter as tk

def parse(file):
    if not file:
        return
    with open(file, "rb") as f:
        for obj in bson.decode_file_iter(f):
            yield obj

def create_fields():
    pass

def main():
    # Create a new tkinter window
    window = tk.Tk()

    # Create a section for personal information
    personal_info_frame = tk.Frame(window)
    personal_info_frame.pack(fill="both", expand=True)

    name_label = tk.Label(personal_info_frame, text="Name:")
    name_label.grid(row=0, column=0)

    name_entry = tk.Entry(personal_info_frame)
    name_entry.grid(row=0, column=1)

    age_label = tk.Label(personal_info_frame, text="Age:")
    age_label.grid(row=1, column=0)

    age_entry = tk.Entry(personal_info_frame)
    age_entry.grid(row=1, column=1)

    # Create a section for address information
    address_frame = tk.Frame(window)
    address_frame.pack(fill="both", expand=True)

    street_label = tk.Label(address_frame, text="Street:")
    street_label.grid(row=0, column=0)

    street_entry = tk.Entry(address_frame)
    street_entry.grid(row=0, column=1)

    city_label = tk.Label(address_frame, text="City:")
    city_label.grid(row=1, column=0)

    city_entry = tk.Entry(address_frame)
    city_entry.grid(row=1, column=1)

    state_label = tk.Label(address_frame, text="State:")
    state_label.grid(row=2, column=0)

    state_entry = tk.Entry(address_frame)
    state_entry.grid(row=2, column=1)

    # Start the main event loop to display the window
    window.mainloop()

if __name__ == "__main__":
    main()

#def main():
#    queues = parse("rtq.bson")
#    custom_fields = parse("custom_fields.bson")
#    root = tk.Tk()
#    root.title("RTQ")
#    root.geometry("800x600")
#    root.mainloop()
#    pass
