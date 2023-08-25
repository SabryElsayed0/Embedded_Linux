import re
from openpyxl import Workbook

# Function to extract function prototypes from the header file
def extract_prototypes(header_file):
    with open(header_file, 'r') as file:
        content = file.read()

    # Use regular expression to extract function prototypes
    pattern = r'\w+\s+\w+\([^;]+\);'
    prototypes = re.findall(pattern, content)
    return prototypes

# Header file to parse
header_file = '/home/sabry/Embedded_Linux/Labs/Tasks_test/header_file.h'  # Replace with the path to your header file

# Extract function prototypes
prototypes = extract_prototypes(header_file)

# Create an Excel workbook and get the active sheet
workbook = Workbook()
sheet = workbook.active

# Insert function prototypes into the Excel sheet with unique IDs
sheet['A1'] = 'ID'
sheet['B1'] = 'Function Prototype'

for i, prototype in enumerate(prototypes, start=0):
    cell_id = f'A{i + 2}'
    cell_prototype = f'B{i + 2}'
    sheet[cell_id] = f'IDX{i}'
    sheet[cell_prototype] = prototype

# Save the workbook
workbook.save('function_prototypes.xlsx')  # Choose a desired filename