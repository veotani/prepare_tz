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
            raise Exception('All CoursePrices values must be initialized.')

        if (self.lectures_price * self.lectures_hours != self.lectures_cost): 
            raise Exception('CoursePrices hours to cost multiplication is not correct.')
        if (self.structure_price * self.structure_cost != self.structure_hours): 
            raise Exception('CoursePrices hours to cost multiplication is not correct.')
        if (self.tests_price * self.tests_cost != self.tests_hours): 
            raise Exception('CoursePrices hours to cost multiplication is not correct.')
        if (self.guidance_price * self.guidance_cost != self.guidance_hours): 
            raise Exception('CoursePrices hours to cost multiplication is not correct.')
        
        if (self.guidance_cost + self.guidance_cost + self.guidance_cost + self.guidance_cost != self.guidance_cost):
            raise Exception('CoursePrices services summ is not equal to total price.')