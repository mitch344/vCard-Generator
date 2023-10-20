import tkinter as tk
from tkinter import ttk, filedialog

def add_contact_row():
    fields = [entry.get() for entry in entries]
    tree.insert('', tk.END, values=tuple(fields))
    for entry in entries:
        entry.delete(0, tk.END)

def generate_vcard():
    rows = list(tree.get_children())
    with open('contacts.vcf', 'w') as file:
        for row in rows:
            values = tree.item(row)['values']
            file.write('BEGIN:VCARD\n')
            file.write('VERSION:3.0\n')
            
            if values[0] or values[1]:
                file.write(f'N:{values[1]};{values[0]};;;\n')
                file.write(f'FN:{values[0]} {values[1]}\n')
            
            if values[2]:
                file.write(f'TEL;CELL:{values[2]}\n')
            
            if values[3]:
                file.write(f'TEL;HOME:{values[3]}\n')
            
            if values[4]:
                file.write(f'ADR;HOME:;;{values[4]}\n')
            
            if values[5]:
                file.write(f'EMAIL:{values[5]}\n')
            
            if values[6]:
                file.write(f'ORG:{values[6]}\n')
            
            if values[7]:
                file.write(f'TITLE:{values[7]}\n')
            
            file.write('END:VCARD\n')

def remove_contact_row():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)

def load_vcard(clear_tree=False):
    file_path = filedialog.askopenfilename(filetypes=[("vCard Files", "*.vcf")])
    if not file_path:
        return

    if clear_tree:
        for row in tree.get_children():
            tree.delete(row)

    with open(file_path, 'r') as file:
        lines = file.readlines()

    contact = {}
    for line in lines:
        if line.startswith("BEGIN:VCARD"):
            contact = {}
        elif line.startswith("END:VCARD"):
            insert_contact(contact)
        else:
            parse_line(line, contact)

def parse_line(line, contact):
    key, _, value = line.partition(":")
    key_main, *key_sub = key.split(";")
    
    mappings = {
        'N': ('Last Name', 'First Name'),
        'FN': 'Full Name',
        'TEL': 'Phone',
        'ADR': 'Address',
        'EMAIL': 'Email',
        'ORG': 'Organization',
        'TITLE': 'Title'
    }
    
    value = value.strip()
    
    if key_main == 'N':
        last, first, *_ = value.split(";")
        contact['First Name'] = first
        contact['Last Name'] = last
    
    elif key_main == 'TEL':
        type_tel = 'Phone'
        if 'CELL' in key_sub:
            type_tel = 'Mobile'
        elif 'HOME' in key_sub:
            type_tel = 'Home Phone'
        contact[type_tel] = value
    
    elif key_main == 'ADR':
        _, _, street, city, state, postal_code, country, *_ = value.split(";") + [""]*7
        contact['Address'] = f"{street}, {city}, {state}, {postal_code}, {country}"
    
    elif key_main in mappings:
        contact[mappings[key_main]] = value
    
    else:
        print(f"Unrecognized key: {key_main}")

def insert_contact(contact):
    values = [contact.get(heading, '') for heading in headings]
    tree.insert('', tk.END, values=tuple(values))

def on_tree_select(event):
    selected = tree.selection()
    if selected:
        values = tree.item(selected)['values']
        for i, entry in enumerate(entries):
            entry.delete(0, tk.END)
            entry.insert(0, values[i])

def update_contact():
    selected = tree.selection()
    if selected:
        new_values = [entry.get() for entry in entries]
        tree.item(selected, values=new_values)


def clear_entries():
    for entry in entries:
        entry.delete(0, tk.END)

root = tk.Tk()
root.title('vCard Generator')

main_frame = ttk.Frame(root, padding='10')
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

entry_frame = ttk.LabelFrame(main_frame, text="Contact Information", padding='10')
entry_frame.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

for i in range(8):
    entry_frame.grid_rowconfigure(i, weight=1)
entry_frame.grid_columnconfigure(1, weight=1)

entry_frame = ttk.LabelFrame(main_frame, text="Contact Information", padding='10')
entry_frame.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

entry_frame.grid_columnconfigure(1, weight=1)

columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8')
tree = ttk.Treeview(main_frame, columns=columns, show='headings')
tree.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

scroll_x = ttk.Scrollbar(main_frame, orient=tk.HORIZONTAL, command=tree.xview)
scroll_x.grid(row=1, column=1, sticky=(tk.W, tk.E))
tree.configure(xscrollcommand=scroll_x.set)

headings = ('First Name', 'Last Name', 'Mobile', 'Home Phone', 'Address', 'Email', 'Organization', 'Title')
for col, heading in zip(columns, headings):
    tree.heading(col, text=heading)
    tree.column(col, stretch=tk.YES)

main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

labels_texts = headings
entries = []

for i, text in enumerate(labels_texts):
    label = ttk.Label(entry_frame, text=f'{text}:')
    label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
    entry = ttk.Entry(entry_frame)
    entry.grid(row=i, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
    entries.append(entry)

button_frame = ttk.Frame(entry_frame)
button_frame.grid(row=len(entries), column=0, columnspan=2, pady=10)

add_button = ttk.Button(button_frame, text='Add Contact', command=add_contact_row)
add_button.grid(row=0, column=0, padx=5, sticky=tk.W)

remove_button = ttk.Button(button_frame, text='Remove Contact', command=remove_contact_row)
remove_button.grid(row=0, column=1, padx=5)

generate_button = ttk.Button(button_frame, text='Generate vCard', command=generate_vcard)
generate_button.grid(row=0, column=2, padx=5)

load_button = ttk.Button(button_frame, text='Load vCard', command=lambda: load_vcard(clear_tree=True))
load_button.grid(row=0, column=3, padx=5)

merge_button = ttk.Button(button_frame, text='Merge vCard', command=lambda: load_vcard(clear_tree=False))
merge_button.grid(row=0, column=4, padx=5)

tree.bind('<<TreeviewSelect>>', on_tree_select)

update_button = ttk.Button(button_frame, text='Update Contact', command=update_contact)
update_button.grid(row=0, column=5, padx=5)

clear_button = ttk.Button(button_frame, text='Clear', command=clear_entries)
clear_button.grid(row=0, column=6, padx=5)

root.mainloop()