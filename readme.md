# Revit Dynamo Sheet Automation

This project contains a Dynamo Python script that automates the creation of Revit sheets and places floor plan and elevation views grouped by their associated levels.

## 🔧 Features

- Automatically detects floor plans and elevations
- Groups views by associated level
- Creates sheets with a clean naming convention
- Places views on sheets with vertical spacing
- Skips already existing sheets (no duplication)

## 📁 Files

- `sheet_automation.py`: Python script used in a Dynamo Python Node

## 💻 Requirements

- Autodesk Revit (tested with 2022/2023+)
- Dynamo (2.6+)
- At least one Title Block family loaded in the Revit project
- Valid floor plan and elevation views with "Associated Level" parameter set

## 🚀 How to Use

1. Open Revit and Dynamo.
2. Create a new Dynamo script.
3. Insert a Python Script Node.
4. Paste code from `sheet_automation.py` into the node.
5. Connect a Boolean toggle to trigger execution.
6. Run the script.


## 🧠 Author

Made by Husnain Rehmat
Expert in Python, AI, and BIM Automation

---

Feel free to use, modify, or contribute to improve this tool.
