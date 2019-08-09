import xlrd

from decimal import Decimal
from models.CourseInfo import CourseInfo

class ExcelPricesParser:
    def __init__(self, filename, author_name_col, course_name_col, cost_col):
        self.filename = filename
        self.author_name_col = author_name_col
        self.course_name_col = course_name_col
        self.cost_col = cost_col

    def parse(self):
        bad_rows = []
        parse_res = []
        excel_document = xlrd.open_workbook(self.filename)
        sheet = excel_document.sheet_by_index(0)
        
        for i in range(1, sheet.nrows):
            if sheet.row(i)[self.course_name_col].value:
                course_name = sheet.row(i)[self.course_name_col].value
            author_name = sheet.row(i)[self.author_name_col].value
            cost = sheet.row(i)[self.cost_col].value

            try:
                Decimal(str(round(cost, 2)))
            except:
                bad_rows.append(i)
                print(f'{author_name}, {course_name} - can\'t get price.')
                continue

            if not course_name:
                bad_rows.append(i)
                raise Exception('The first row should have course name.')
            
            course_info = CourseInfo(course_name, author_name, cost)

            if len(author_name) == 0  or not (Decimal(str(round(float(cost), 2))) > 0):
                bad_rows.append(i)                
                continue

            parse_res.append(course_info)
        
        bad_rows_str = ' '.join(list(map(lambda x: str(x), bad_rows)))
        report = 'Bad rows are: ' + bad_rows_str

        print(report)
        
        return parse_res

        
