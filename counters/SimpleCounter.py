from decimal              import *
from models.CoursePrices  import CoursePrices

'''
Service to count prices, costs and hours per each job.
'''

class SimpleCounter:
    def __init__(self):
        pass

    def get_course_model(self, course_info):
        rounded_cost = Decimal(str(round(course_info.cost, 2)))

        lectures_cost  = 80 * (rounded_cost // 100)
        structure_cost = 5 *  (rounded_cost // 100)
        guidance_cost  = 5 *  (rounded_cost // 100)
        tests_cost     = rounded_cost - (lectures_cost + structure_cost + guidance_cost)

        lectures_price  = Decimal('800')
        structure_price = Decimal('100')
        guidance_price  = Decimal('100')
        tests_hours     = Decimal('0')

        for i in range(1, 50):
            if int(tests_cost * 100) % i == 0:
                tests_hours = i
        
        if tests_hours == 0:
            raise Exception(f'There is no divisor for tests cost. Cost is {tests_cost}.')
        
        lectures_hours  = lectures_cost / lectures_price
        structure_hours = structure_cost / structure_price
        guidance_hours  = guidance_cost / guidance_price
        tests_price     = tests_cost / tests_hours

        course_prices = CoursePrices(
            lectures_price, lectures_hours, lectures_cost, 
            structure_price, structure_cost, structure_hours, 
            tests_price, tests_cost, tests_hours,
            guidance_price, guidance_cost, guidance_hours,
            rounded_cost,
            course_info.author_name, course_info.course_name
        )

        return course_prices
        