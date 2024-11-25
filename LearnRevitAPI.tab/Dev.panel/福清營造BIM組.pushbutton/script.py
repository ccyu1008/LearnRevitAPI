# -*- coding: utf-8 -*-
__title__ = "福清浮水印命名機"
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
# Prompt user to select views
selected_views = forms.select_views(title="選擇要重新命名的視圖", multiple=True)

# Ensure views are selected
if not selected_views:
    forms.alert("請選擇至少一個視圖以重新命名。", exitscript=True)

# Start a transaction to rename views
doc = revit.doc
t = Transaction(doc, "Rename Selected Views")
t.Start()

try:
    for view in selected_views:
        # Get the required parameters
        cde_status_param = view.LookupParameter("CDE狀態")
        cde_status = cde_status_param.AsString() if cde_status_param and cde_status_param.AsString() else "未定義"

        main_category_param = view.LookupParameter("主分類")
        main_category = main_category_param.AsString() if main_category_param and main_category_param.AsString() else "未定義"

        sub_category_param = view.LookupParameter("次分類")
        sub_category = sub_category_param.AsString() if sub_category_param and sub_category_param.AsString() else "未定義"

        associated_level_param = view.LookupParameter("關聯的樓層")
        associated_level = associated_level_param.AsString() if associated_level_param and associated_level_param.AsString() else "未定義"

        # Construct the new name
        new_name = "{}_{}_{}_{}".format(cde_status, main_category, sub_category, associated_level)

        try:
            # Rename the view
            view.Name = new_name
            print("視圖 '{}' 已被重新命名為 '{}'".format(view.Id, new_name))
        except Exception as e:
            # Handle errors (e.g., duplicate names)
            print("無法重命名視圖 '{}': {}".format(view.Id, str(e)))
            continue
finally:
    t.Commit()

forms.alert("視圖重命名已完成！")