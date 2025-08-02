import clr

# Revit/Dynamo API references
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

# Get current document
doc = DocumentManager.Instance.CurrentDBDocument

# Collect all views
views = FilteredElementCollector(doc).OfClass(View).ToElements()

# Separate floor plans and elevations (exclude templates)
floor_plans = [v for v in views if v.ViewType == ViewType.FloorPlan and not v.IsTemplate]
elevations = [v for v in views if v.ViewType == ViewType.Elevation and not v.IsTemplate]

# Group views by associated level
grouped_views = {}

def group_by_level(view_list):
    for view in view_list:
        level_param = view.LookupParameter("Associated Level")
        if level_param and level_param.HasValue:
            level_name = level_param.AsString()
            if level_name not in grouped_views:
                grouped_views[level_name] = []
            grouped_views[level_name].append(view)

group_by_level(floor_plans)
group_by_level(elevations)

# Get the first available title block
title_block = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_TitleBlocks).FirstElement()

# Collect existing sheet names to avoid duplicates
existing_sheets = [s.Name for s in FilteredElementCollector(doc).OfClass(ViewSheet).ToElements()]

# Start transaction
TransactionManager.Instance.EnsureInTransaction(doc)

created_sheets = []

# Create sheets and place views
for level, views_on_level in grouped_views.items():
    sheet_name = "Level - " + level
    if sheet_name in existing_sheets:
        continue  # Skip if sheet already exists

    # Create new sheet
    sheet = ViewSheet.Create(doc, title_block.Id)
    sheet.Name = sheet_name
    created_sheets.append(sheet)

    # Place views on the sheet (stacked vertically)
    for i, view in enumerate(views_on_level):
        try:
            location = XYZ(0, i * 2.5, 0)
            Viewport.Create(doc, sheet.Id, view.Id, location)
        except:
            continue  # Skip views that can't be placed

# End transaction
TransactionManager.Instance.TransactionTaskDone()

# Output the created sheets
OUT = created_sheets
