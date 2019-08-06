'''
Course information model.

This is the information that input files must contain.
'''

class CourseInfo:
    def __init__(self, course_name, author_name, cost):
        self.course_name = course_name
        self.author_name = author_name
        self.cost        = cost
