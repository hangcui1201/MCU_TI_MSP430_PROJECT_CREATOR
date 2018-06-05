from tkinter import *
from MSP430ProjectCreator.ProjectCreatorGUI import ProjectCreatorGUI

# change this file name from MSP430ProjectCreator.py to __main__.py
# make this directory executable

root = Tk()
new_project = ProjectCreatorGUI(root)
root.mainloop()