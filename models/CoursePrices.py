'''
Course prices model.

Model class contains infomation about payment for an author of the online course and the name of the course. 
The values are tested after initialization.
'''

class CoursePrices:
    def __init__(self, 
        lectures_price, lectures_hours, lectures_cost, 
        structure_price, structure_cost, structure_hours, 
        tests_price, tests_cost, tests_hours,
        guidance_price, guidance_cost, guidance_hours,
        total_cost,
        author_name, course_name
    ):

        self.lectures_price = lectures_price
        self.lectures_cost  = lectures_cost
        self.lectures_hours = lectures_hours

        self.structure_price = structure_price
        self.structure_cost  = structure_cost
        self.structure_hours = structure_hours

        self.tests_price = tests_price
        self.tests_cost  = tests_cost
        self.tests_hours = tests_hours

        self.guidance_price = guidance_price
        self.guidance_cost  = guidance_cost
        self.guidance_hours = guidance_hours

        self.author_name = author_name
        self.course_name = course_name

        self.total_cost = total_cost

        self.testModel()

    def testModel(self):
        """
        Check if prices are correct and initialized.
        """
        if not (
            self.lectures_price and self.lectures_hours and self.lectures_cost and
            self.structure_price and self.structure_cost and self.structure_hours and
            self.tests_price and self.tests_cost and self.tests_hours and
            self.guidance_price and self.guidance_cost and self.guidance_hours and
            self.total_cost
        ):
            raise Exception(f'All CoursePrices values must be initialized. My table is\n{self.__str__()}')

        if (self.lectures_price * self.lectures_hours != self.lectures_cost): 
            raise Exception('Lecture hours to cost multiplication is not correct.')
        if (self.structure_price * self.structure_hours != self.structure_cost): 
            raise Exception('Structure hours to cost multiplication is not correct.')
        if (self.tests_price * self.tests_hours != self.tests_cost): 
            raise Exception('Tests hours to cost multiplication is not correct.')
        if (self.guidance_price * self.guidance_hours != self.guidance_cost): 
            raise Exception('Guidance hours to cost multiplication is not correct.')
        
        if (self.lectures_cost + self.structure_cost + self.guidance_cost + self.tests_cost != self.total_cost):
            raise Exception('CoursePrices services summ is not equal to total price.')

    def __str__(self):
        representation = f'{self.author_name}\n' + \
            f'{self.course_name}\n' + \
            f'{self.lectures_price}\t{self.lectures_hours}\t{self.lectures_cost}\n' + \
            f'{self.structure_price}\t{self.structure_hours}\t{self.structure_cost}\n' + \
            f'{self.guidance_price}\t{self.guidance_hours}\t{self.guidance_cost}\n' + \
            f'{self.tests_price}\t{self.tests_hours}\t{self.tests_cost}\n' + \
            f' \t \t{self.total_cost}'
        return representation