'''
Course information model.

This is the information that input files must contain.
'''

from num2words import num2words
from datetime import datetime


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
        degree,
        address_by_pasport,
        telephone_number,
        reward,
        insurance,
        birthdate,
        job_name,
        bank_name
    ):
        # Convert dates
        if type(passport_created_date) == float or type(passport_created_date) == int:
            passport_created_date = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(passport_created_date) - 2).date()
        if type(tax_start_date) == float or type(tax_start_date) == int:
            tax_start_date = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(tax_start_date) - 2).date()
        if type(birthdate) == float or type(birthdate) == int:
            birthdate = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(birthdate) - 2).date()
        
            
        self.address_by_pasport = address_by_pasport
        self.telephone_number = telephone_number

        self.job_name = job_name
        self.bank_name = bank_name

        self.course_name = course_name
        self.author_name = author_name  
        self.author_second_name = author_name.split(' ')[0]
        self.author_first_name = author_name.split(' ')[1]
        self.author_middle_name = author_name.split(' ')[2]

        self.cost        = cost
        if len(str(cost).split('.')) == 2:
            self.contract_price_rub = int(str(cost).split('.')[0])
            self.contract_price_cent = int(str(cost).split('.')[1])
        else:
            self.contract_price_rub = int(cost)
            self.contract_price_cent = 0
        self.contract_price_rub_in_words = num2words(self.contract_price_rub, lang='ru')
        self.contract_price_cent_in_words = num2words(self.contract_price_cent, lang='ru')

        self.reward      = reward
        if len(str(reward).split('.')) == 2:
            self.author_reward_rub = int(str(reward).split('.')[0])
            self.author_reward_cent = int(str(reward).split('.')[1])
        else:
            self.author_reward_rub = int(reward)
            self.author_reward_cent = 0
        self.author_reward_rub_in_words = num2words(self.author_reward_rub, lang='ru')
        self.author_reward_cent_in_words = num2words(self.author_reward_cent, lang='ru')

        if len(str(insurance).split('.')) == 2:
            self.insurance_rub = int(str(insurance).split('.')[0])
            self.insurance_cent = int(str(insurance).split('.')[1])
        else:
            self.insurance_rub = int(insurance)
            self.insurance_cent = 0
        self.insurance_rub_in_words = num2words(self.insurance_rub, lang='ru')
        self.insurance_cent_in_words = num2words(self.insurance_cent, lang='ru')

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
            
        self.itn_1 = str(self.ITN)[0]
        self.itn_2 = str(self.ITN)[1]
        self.itn_3 = str(self.ITN)[2]
        self.itn_4 = str(self.ITN)[3]
        self.itn_5 = str(self.ITN)[4]
        self.itn_6 = str(self.ITN)[5]
        self.itn_7 = str(self.ITN)[6]
        self.itn_8 = str(self.ITN)[7]
        self.itn_9 = str(self.ITN)[8]
        self.itn_10 = str(self.ITN)[9]
        self.itn_11 = str(self.ITN)[10]
        self.itn_12 = str(self.ITN)[11]
        self.inila_1 = str(self.INILA)[0]
        self.inila_2 = str(self.INILA)[1]
        self.inila_3 = str(self.INILA)[2]
        self.inila_4 = str(self.INILA)[3]
        self.inila_5 = str(self.INILA)[4]
        self.inila_6 = str(self.INILA)[5]
        self.inila_7 = str(self.INILA)[6]
        self.inila_8 = str(self.INILA)[7]
        self.inila_9 = str(self.INILA)[8]
        self.inila_10 = str(self.INILA)[9]
        self.inila_11 = str(self.INILA)[10]