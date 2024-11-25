# -*- coding: utf-8 -*-
__title__ = "RenamePractice"
__doc__ = """Version = 1.0
Date    = 15.07.2024
_____________________________________________________________________
Description:
This is a template file for pyRevit Scripts.
_____________________________________________________________________
How-to:
-> Click on the button
-> Select View
Define Renaming Rules
Rename Views
_____________________________________________________________________
Last update:
- [22.11.2024] - 1.0 RELEASE
_____________________________________________________________________
To-Do:
- Describe Next Features
_____________________________________________________________________
Author: Erik Frits"""

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
#==================================================
# Regular + Autodesk
from Autodesk.Revit.DB import *


# pyRevit
from pyrevit import revit, forms

# .NET Imports (You often need List import)

import clr
from pyrevit.forms import select_views

clr.AddReference("System")
from System.Collections.Generic import List

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
#==================================================
from Autodesk.Revit.UI import UIDocument
doc   = __revit__.ActiveUIDocument.Document #type: Document
uidoc = __revit__.ActiveUIDocument          #type: UIDocument
app   = __revit__.Application               #type: Application

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝
#==================================================

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
#==================================================
# START CODE HERE
print('Template has been developed by 福清營造BIM組俞承中.')

#1️⃣GetViews
sel_el_ids = uidoc.Selection.GetElementIds()
sel_elem   = [doc.GetElement(e_id) for e_id in sel_el_ids]
sel_views = [el for el in sel_elem if issubclass(type(el), View)]

#If not, Show forms

if not sel_views:
    sel_elem = forms.select_views()

#Ensure Views Selected
if not sel_views:
    forms.alert('沒有選到任何視圖',exitscript=True)

#Define Renaming Rules
#previx,find,replace,suffix

from rpw.ui.forms import (FlexForm, Label, TextBox, Separator, Button)
components = [Label('Prefix:'),  TextBox('prefix'),
              Label('Find:'),    TextBox('find'),
              Label('Replace:'), TextBox('replace'),
              Label('Suffix:'),  TextBox('suffix'),
              Separator(),       Button('Rename Views')]



form = FlexForm('Title', components)
form.show()

user_inputs = form.values #type: dict
prefix      = user_inputs['prefix']
find        = user_inputs['find']
replace     = user_inputs['replace']
suffix      = user_inputs['suffix']

Transaction(doc,'py-Rename Views')
t.Start()


t.Commit()

for view in sel_views:
    #create new view name
    old_name = view.Name
    new_name = old_name.replace(find, replace) + suffix
    #rename view and ensure unique view name
    view.Name = new_name
    for i in range(20):
    try:
        view.Name = new_name
    except:
        new_name += '*'




print ('完成！')