import xlrd
from xlutils.copy import copy


class ExcelConverter:
    def __init__(self, file_path, sheet_name=0):
        self.sheet_name = sheet_name
        self.path = file_path
        self.excel_r = xlrd.open_workbook(file_path)
        try:
            self.sheet = self.excel_r.sheet_by_index(0) if isinstance(sheet_name, int) else self.excel_r.sheet_by_name(sheet_name)
        except:
            raise RuntimeError("Can't find the sheet name: " + str(self.sheet_name))
        self.excel_w = copy(self.excel_r)
        self.rsheet = self.excel_w.get_sheet(self.sheet_name)
        self.rsheet.encoding = "utf-8"
        # 检查文件的标题是否正确
        try:
            a = self.sheet.row_values(0)
            assert a == [u'\u6807\u9898', u'case\u7c7b\u578b',
                         u'\u8bf7\u6c42\u65b9\u5f0f\uff08get/post form/post raw\uff09', u'\u8bf7\u6c42\u7684url',
                         u'\u8bf7\u6c42\u53c2\u6570\uff08\u5199\u6210json\u683c\u5f0f\uff09',
                         u'\u7279\u5b9a\u7684user agent',
                         u'\u8bf7\u6c42\u7684header\uff08\u5199\u6210json\u683c\u5f0f\uff09',
                         u'\u9884\u671f\u7684\u8fd4\u56de\u7ed3\u679c',
                         u'\u6700\u5927\u91cd\u8bd5\u6b21\u6570\uff08\u9ed8\u8ba42\uff09', u'\u6d4b\u8bd5\u7ed3\u679c',
                         u'\u5b9e\u9645\u7684\u8fd4\u56de\u7ed3\u679c', u'\u6d4b\u8bd5\u6b21\u6570',
                         u'\u7ed3\u679c\u8be6\u60c5']

        except AssertionError as e:
            raise RuntimeError("Check out the title on the first line: \n" + e.message)

    def read_case(self):
        # 检查读入的格式；

        # 向DB中插入数据；
        pass

    def write_result(self):
        pass

if __name__ == "__main__":
    e = ExcelConverter("D:/my first task.xlsx")
    print(e.sheet.row_values(0))
