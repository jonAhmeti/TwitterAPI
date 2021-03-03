import openpyxl
import os

xl = openpyxl.load_workbook('worldcities.xlsx')

countries = set()

for row in xl['Sheet1'].iter_rows():
    for cell in row:
        if cell.col_idx == 4:
            countries.add(cell.value)

for country in countries:
    with open(f'Locations\\{country}.py', 'w') as creator:
        creator.write(f'class {country}:\n')

countryFiles = [f for f in os.listdir('Locations') if
                os.path.isfile(os.path.join('D:\\PycharmProjects\\TwitterAPI\\Locations', f))]

for row in xl['Sheet1'].iter_rows():
    celldata = '    '
    for cell in row:
        if cell.col_idx == 1:
            celldata += f'{cell.value} = \''
        elif cell.col_idx == 2:
            celldata = celldata + f'{cell.value},'
        elif cell.col_idx == 3:
            celldata = celldata + str(cell.value)
        for filePath in os.listdir('Locations'):
            if cell.col_idx == 4 and filePath.split('.')[0] == cell.value:
                celldata += '\''
                with open(f'Locations\\{filePath}', 'a', encoding='utf-8') as writer:
                    writer.write('\n' + celldata + '\n')
