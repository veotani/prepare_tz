from decimal              import *
from models.CoursePrices  import CoursePrices

'''
Service to count prices, costs and hours per each job.
'''

class SimpleCounter:
    def __init__(self):
        pass

    def getCourseModel(self, cost, author_name, course_name):
        rounded_cost = round(cost, 2)

        lectures_cost  = 80 * rounded_cost // 100
        structure_cost = 5 * rounded_cost // 100
        guidance_cost  = 5 * rounded_cost // 100
        tests_cost     = Decimal(rounded_cost) - (Decimal(lectures_cost) + Decimal(structure_cost) + Decimal(guidance_cost))

        lectures_price  = 800
        structure_price = 100
        guidance_price  = 100
        tests_price     = 0

        for i in range(100, 500):
            if int(tests_cost * 100) % i == 0:
                tests_price = i
                break
        
        if tests_price == 0:
            raise Exception('There is no divisor for tests cost.')
        
        lectures_hours  = lectures_cost / lectures_price
        structure_hours = structure_cost / structure_price
        guidance_hours  = guidance_cost / guidance_price
        tests_hours     = tests_cost / tests_price

        course_prices = CoursePrices(
            lectures_price, lectures_hours, lectures_cost, 
            structure_price, structure_cost, structure_hours, 
            tests_price, tests_cost, tests_hours,
            guidance_price, guidance_cost, guidance_hours,
            rounded_cost,
            author_name, course_name
        )

        return course_prices
        