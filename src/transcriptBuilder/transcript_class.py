# Connor Morgandale
# Will be called by transcript_organzier.py and checksheet_to_node.py for each class 
# from the parsed transcript and checksheet classes.


class Course:
    def __init__(self, dept, course, name, credit):
        self.dept = dept
        self.course = course
        self.name = name
        self.credit = credit
