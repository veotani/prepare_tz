import xlrd

from models.CourseInfo import CourseInfo

class ExcelPricesParser:
    def __init__(self, filename, author_name_col, course_name_col, cost_col):
        self.filename = filename
        self.author_name_col = author_name_col
        self.course_name_col = course_name_col
        self.cost_col = cost_col

    def parse(self):
        parse_res = []
        excel_document = xlrd.open_workbook(self.filename)
        sheet = excel_document.sheet_by_index(0)
        
        for i in range(1, sheet.nrows):
            if sheet.row(i).value:
                course_name = sheet.row(i)[self.course_name_col].value
            author_name = sheet.row(i)[self.author_name_col]
            cost = sheet.row(i)[self.cost_col]

            if not course_name:
                raise Exception('The first row should have course name.')
            
            course_info = CourseInfo(course_name, author_name, cost)

            parse_res.append(course_info)
        
        return parse_res

        
