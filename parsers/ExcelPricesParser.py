import xlrd

from decimal import Decimal
from models.CourseInfo import CourseInfo

class ExcelPricesParser:
    def __init__(
        self, 
        filename, 
        author_name_col, 
        course_name_col, 
        cost_col, 
        reward_col,
        birthdate_col,
        passport_seria_number_col,
        passport_created_location_col,
        passport_created_date_col,
        ITN_col,
        INILA_col,
        tax_start_date_col,
        position_col,
        bank_requisites_col,
        degree_col,
        address_by_pasport_col,
        telephone_number_col
    ):
        self.filename = filename
        self.author_name_col = author_name_col
        self.course_name_col = course_name_col
        self.cost_col = cost_col
        self.reward_col = reward_col
        self.birthdate_col = birthdate_col
        self.passport_seria_number_col = passport_seria_number_col
        self.passport_created_location_col = passport_created_location_col
        self.passport_created_date_col = passport_created_date_col
        self.ITN_col = ITN_col
        self.INILA_col = INILA_col
        self.tax_start_date_col = tax_start_date_col
        self.position_col = position_col
        self.bank_requisites_col = bank_requisites_col
        self.degree_col = degree_col
        self.address_by_pasport_col = address_by_pasport_col
        self.telephone_number_col = telephone_number_col
        self.reward_col = reward_col

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
            except Exception as e:
                bad_rows.append(i)
                print(f'{author_name}, {course_name} - can\'t get price.')
                print(f'Exception: {str(e)}')
                continue
            # TODO: Read about scopes in python. Not sure that cost can be assigned inside "try" 
            # block to work with it further
            cost = Decimal(str(round(cost, 2)))

            if not course_name:
                bad_rows.append(i)
                raise Exception('The first row should have course name.')

            birthdate = sheet.row(i)[self.birthdate_col].value
            passport_seria_number = sheet.row(i)[self.passport_seria_number_col].value
            passport_created_location = sheet.row(i)[self.passport_created_location_col].value
            passport_created_date = sheet.row(i)[self.passport_created_date_col].value
            ITN = sheet.row(i)[self.ITN_col].value
            INILA = sheet.row(i)[self.INILA_col].value
            tax_start_date = sheet.row(i)[self.tax_start_date_col].value
            position = sheet.row(i)[self.position_col].value
            bank_requisites = sheet.row(i)[self.bank_requisites_col].value
            degree = sheet.row(i)[self.degree_col].value
            address_by_pasport = sheet.row(i)[self.address_by_pasport_col].value
            telephone_number = sheet.row(i)[self.telephone_number_col].value

            reward = float(sheet.row(i)[self.reward_col].value)
            try:
                reward = Decimal(str(round(reward, 2)))
            except:
                bad_rows.append(i)
                print(f'{author_name}, {course_name} - can\'t get reward.')
                continue
            # TODO: Read about scopes in python. Not sure that reward can be assigned inside "try" 
            # block to work with it further
            reward = Decimal(str(round(reward, 2)))

            insurance = cost - reward
            birthdate = sheet.row(i)[self.birthdate_col].value

            try:
                str(ITN)[11]
            except:
                #print(f'{author_name}, {course_name} - can\'t get ITN.')
                ITN = " " * 12
            
            INILA = str(INILA).replace('-', '').replace(' ', '')
            try:
                str(INILA)[10]
            except:
                #print(f'{author_name}, {course_name} - can\'t get INILA.')
                INILA = " " * 11
            
            if len(author_name.split(' ')) < 3:
                if len(author_name.split(' ')) == 2:
                    if len(author_name.split(' ')[1]) > 1:
                        author_name += ' '
                else:
                    print(f'{author_name}, {course_name} - name is incorrect.')
                    continue
            
            course_info = CourseInfo(
                course_name = course_name, 
                author_name = author_name, 
                cost = cost,
                passport_seria_number = passport_seria_number,
                passport_created_location = passport_created_location,
                passport_created_date = passport_created_date,
                ITN = ITN,
                INILA = INILA,
                tax_start_date = tax_start_date,
                position = position,
                bank_requisites = bank_requisites,
                degree = degree,
                address_by_pasport = address_by_pasport,
                telephone_number = telephone_number,
                reward = reward,
                insurance = insurance,
                birthdate = birthdate                
            )

            if len(author_name) == 0  or not (Decimal(str(round(float(cost), 2))) > 0):
                bad_rows.append(i)                
                continue

            parse_res.append(course_info)
        
        bad_rows_str = ' '.join(sorted(list(map(lambda x: str(x), bad_rows))))
        report = 'Bad rows are: ' + bad_rows_str

        print(report)
        
        return parse_res

        
