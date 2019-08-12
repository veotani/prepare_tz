'''
Course information model.

This is the information that input files must contain.
'''

class CourseInfo:
    def __init__(self, course_name, author_name, cost,
        passport_seria_number,
        passport_created_location,
        passport_created_date,
        ITN,
        INILA,
        tax_start_date,
        position,
        bank_requisites,
        degree
    ):
        self.course_name = course_name
        self.author_name = author_name
        self.cost        = cost
        self.reward      = reward
        self.birthdate   = birthdate
        self.passport_seria_number = passport_seria_number
        self.passport_created_location = passport_created_location
        self.passport_created_date = passport_created_date
        self.ITN = ITN
        self.INILA = INILA
        self.tax_start_date = tax_start_date
        self.position = position
        self.bank_requisites = bank_requisites
        self.degree = degree
            
        self.itn_1 = self.ITN[0]
        self.itn_2 = self.ITN[1]
        self.itn_3 = self.ITN[2]
        self.itn_4 = self.ITN[3]
        self.itn_5 = self.ITN[4]
        self.itn_6 = self.ITN[5]
        self.itn_7 = self.ITN[6]
        self.itn_8 = self.ITN[7]
        self.itn_9 = self.ITN[8]
        self.itn_10 = self.ITN[9]
        self.itn_11 = self.ITN[10]
        self.itn_12 = self.ITN[11]
        self.inila_1 = self.INILA[0]
        self.inila_2 = self.INILA[1]
        self.inila_3 = self.INILA[2]
        self.inila_4 = self.INILA[3]
        self.inila_5 = self.INILA[4]
        self.inila_6 = self.INILA[5]
        self.inila_7 = self.INILA[6]
        self.inila_8 = self.INILA[7]
        self.inila_9 = self.INILA[8]
        self.inila_10 = self.INILA[9]
        self.inila_11 = self.INILA[10]