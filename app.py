from tkinter import *
from tkinter import ttk
import re


pattern_sql = re.compile('INSERT[\s]*INTO[\s]*(\S+).*\((.*?)\).*VALUES(.*)', re.IGNORECASE)


def sql_changed(sql):
    sql_treeview.delete(*sql_treeview.get_children())
    match = pattern_sql.match(sql.get())
    if not match:
        return
    table_name_sql = (match.group(1)).strip()
    fields_sql = (match.group(2)).strip()
    values_sql = (match.group(3)).strip(' ()')

    table_name_label['text'] = f"Table: {table_name_sql}"

    fields = [field.strip() for field in fields_sql.split(',')]

    brackets = 0
    commas = [0]
    for i, l in enumerate(values_sql):
        if l == ',' and brackets == 0:
            commas.append(i+1)
        elif l in '()':
            brackets += {'(': 1, ')': -1}[l]
    if brackets != 0:
        return
    values = [(values_sql[i:j]).strip(' ,') for i,j in zip(commas, commas[1:]+[None])]


    for field, value in zip(fields, values):
        sql_treeview.insert(parent='', index='end', text='', values=(field, value))


def row_selected(a):
    current_item = sql_treeview.focus()
    value = str(sql_treeview.item(current_item)['values'][1])
    search_index = (sql.get()).find(value)
    sql_entry.focus()
    sql_entry.selection_range(search_index, search_index+len(value))
    sql_entry.icursor(search_index+len(value))


root = Tk()
root.title("Finsert")
mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sql = StringVar()
sql_entry = ttk.Entry(mainframe, width=300, textvariable=sql)
sql_entry.grid(column=1, row=1, sticky=(N, W, E))
sql.trace("w", lambda name, index, mode, sql=sql: sql_changed(sql))

table_name_label = ttk.Label(mainframe, text="Table:")
table_name_label.grid(column=1, row=2, sticky=W)

sql_treeview = ttk.Treeview(mainframe, height=35)
sql_treeview.grid(column=1, row=3, sticky=(W, E, S))
sql_treeview['columns'] = ('field', 'value')
sql_treeview.column("#0", width=0,  stretch=NO)
sql_treeview.column("field", anchor=CENTER, width=80)
sql_treeview.column("value", anchor=CENTER, width=80)
sql_treeview.heading("#0", text="", anchor=CENTER)
sql_treeview.heading("field", text="Field", anchor=CENTER)
sql_treeview.heading("value", text="Name", anchor=CENTER)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

sql_entry.focus()
sql_treeview.bind('<ButtonRelease-1>', row_selected)


root.mainloop()
