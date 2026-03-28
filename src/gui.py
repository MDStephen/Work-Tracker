from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# Functions
def browse_path():
    t_path = filedialog.askdirectory()
    if t_path:
        path_input.set(t_path)

def change_log():
    pass

def open_log_path():
    pass

def add_tracking(input_type):
    pass

# Global Variables
global log_path
global log_name

# Setting up the window, and the mainframe which contains everything
window      = Tk("Work_Tracker")
mainframe   = ttk.Frame(window)
mainframe.grid(column=0, row=0, sticky=(N, E, S, W), padx=5, pady=5)

# Setting widgets and their positioning
# Row 1
ttk.Label(mainframe, text="Add new folder for tracking:").grid(column=1, row=1, sticky=(N, W))
separator_v = ttk.Separator(mainframe, orient="vertical")
separator_v.grid(column=2, row=1, rowspan=2, sticky=(N, S), padx=5, pady=5)
ttk.Label(mainframe, text="Add new website for tracking:").grid(column=3, row=1, sticky=(N, W))

# Row 2
path_input =    StringVar()
website_link =  StringVar()
path_frame =    ttk.Frame(mainframe)
website_frame = ttk.Frame(mainframe)
path_frame.grid(    column=1, row=2)
website_frame.grid( column=3, row=2)
path_entry =    ttk.Entry(path_frame, width=30, textvariable=path_input)
path_entry.grid(column=1, row=1, sticky=W)
ttk.Button(path_frame, text="file", command=browse_path).grid(column=2, row=1, sticky=W)
ttk.Button(path_frame, text="add", command=add_tracking("folder")).grid(column=3, row=1, sticky=W)
website_entry = ttk.Entry(website_frame, width=30, textvariable=website_link)
website_entry.grid(column=1, row=1, sticky=E)
ttk.Button(website_frame, text="add", command=add_tracking("website")).grid(column=2, row=1, sticky=W)

# Row 3
separator_h = ttk.Separator(mainframe, orient="horizontal")
separator_h.grid(column=1, row=3, columnspan=3, sticky=(W, E), padx=5, pady=5)

# Row 4
ttk.Label(mainframe, text="Current Log").grid(column=1, row=4, sticky=(N, W))
btn_frame = ttk.Frame(mainframe)
btn_frame.grid(column=3, row=4, sticky=E)
ttk.Button(btn_frame, text="Change Log", command=change_log).grid(column=1, row=1, sticky=E)
ttk.Button(btn_frame, text="Open File Path", command=open_log_path).grid(column=2, row=1, sticky=E)

# Row 5
log_display = Text(mainframe)
log_display.grid(column=1, row=5, columnspan=3)
# Add log content line by line before the state is disabled

log_display['state'] = 'disabled'

# Grid configuration
mainframe.columnconfigure(2, minsize=25)

window.mainloop()