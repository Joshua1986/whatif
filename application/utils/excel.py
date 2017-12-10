import xlrd
from xlutils.copy import copy


class Excel:
    def __init__(self, file_path, sheet_name=0):
        self.sheet_name = sheet_name
        self.path = file_path
        self.data = xlrd.open_workbook(file_path)
        self.sheet = self.data.sheet_by_name(sheet_name) if sheet_name else self.data.sheet_by_index(0)
        self.row = self.sheet.nrows
        self.wb = copy(self.data)
        self.rsheet = self.wb.get_sheet(self.sheet_name)
        self.rsheet.encoding = "utf-8"

    def set_sheet_by_name(self, name):
        self.sheet = self.data.sheet_by_name(name)

    def set_sheet_by_index(self, index):
        self.sheet = self.data.sheet_by_index(index)

    def get_row(self, row_num):
        return self.sheet.row_values(row_num)

    def get_column(self, column_num):
        return self.sheet.col_values(column_num)

    def get_cell_by_index(self, row, col):
        return self.sheet.cell(row, col).value

    def get_cell_by_name(self, cell_name):
        col = int(ord(cell_name.upper()[0])) - 65
        row = int(cell_name[1:]) - 1
        return self.sheet.cell(row, col).value

    def set_cell_by_index(self, row, col, value):
        self.rsheet.write(row, col, value.decode("utf8"))
        self.wb.save(self.path)

    def set_cell_by_name(self, cell_name, value):
        col = int(ord(cell_name.upper()[0])) - 65
        row = int(cell_name[1:]) - 1
        self.rsheet.write(row, col, value.decode('utf8'))
        self.wb.save(self.path)

    def set_cells(self, data_dict):
        if not isinstance(data_dict, dict):
            raise RuntimeError("Parameter data_dict should be a dictionary!")
        for k, v in data_dict.items():
            self.set_cell_by_name(k, v)


if __name__ == "__main__":
    e = Excel("D:/my first task.xlsx")
    print(e.row)
    print(e.get_row(0))
    print(e.get_column(0))
    print(e.get_cell_by_index(1, 1))
    e.set_cell_by_index(1, 1, "ABC")
    print(e.get_cell_by_index(1, 1))
    e.set_cell_by_name("A1", u"标题A")
    print(e.get_cell_by_name("A1"))
