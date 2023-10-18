class PlanOfStudy:
    def __init__(self):
        self.courses = set() # used set here becuase if i do not want the outputs to be duplicated as given in the question

    def add(self, course): #This function will just add the courses to the list
        self.courses.add(course)
        return self

    def get700CSCredits(self): #checks if the course is 700 level and if it is CS subject and will add to the total credits
        total_credits = 0
        for course in self.courses:
            if course.is700Level() and course.isCS():
                total_credits += course.credits
        return total_credits

    def getNonCSCredits(self):#checks if the course is non cs and it will add them to total credits
        total_credits = 0
        for course in self.courses:
            if not course.isCS():
                total_credits += course.credits
        return total_credits

    def getCSGradCredits(self): ##checks if the course is a grad level course and will add credits to it
        total_credits = 0
        for course in self.courses:
            if course.isGradLevel() and course.isCS():
                total_credits += course.credits
        return total_credits

    def isAcceptable(self): # this will see all the conditions and then returh if the courses and credits you took are value or not
        total_credits = sum(course.credits for course in self.courses)
        cs_credits = self.get700CSCredits()
        non_cs_credits = self.getNonCSCredits()
        return cs_credits >= 15 and non_cs_credits <= 9 and total_credits == 30

    def __str__(self): # this is used to format in the we want them to be in the set
        course_names = [f'{course.subject}{course.number}' for course in self.courses]
        return ', '.join(course_names)
class Course:
    def __init__(self, subject, number, credits): #initializing all the siubjects,numbers and courses
        self.subject = subject
        self.number = number
        self.credits = credits

    def __str__(self):
        return f'{self.subject} {self.number} {self.credits} credits'

    def __eq__(self, other): #this will check if the subject and number are same or not for 2 courses
        return self.subject == other.subject and self.number == other.number

    def __hash__(self): # to return the hashvalue to the __eq__
        return hash((self.subject, self.number))

    def isCS(self): # to check if the subject is CS or not
        return self.subject == 'CompSci'

    def is700Level(self): # to check if the subject is 700 level or not
        if isinstance(self.number, int):
            return self.number >= 700
        return False

    def isGradLevel(self): #to check if the course is grad level or not
        if isinstance(self.number, str):
            return self.number[-1] == 'G'
        return True


# Create Course instances
cs431 = Course('CompSci', '431G', 3)
cs481 = Course('CompSci', '481G', 3)
cs535 = Course('CompSci', '535G', 3)
cs715 = Course('CompSci', 715, 3)
cs720 = Course('CompSci', 720, 3)
cs723 = Course('CompSci', 723, 3)
cs732 = Course('CompSci', 732, 3)
cs743 = Course('CompSci', 743, 3)
cs790 = Course('CompSci', 790, 3)
hca740 = Course('HCA', 740, 3)
hca742 = Course('HCA', 742, 3)
hca745 = Course('HCA', 745, 3)

print("The below is the output for the 1st test case")
plan = PlanOfStudy()
plan.add(cs431).add(cs481).add(cs535)\
.add(cs715).add(cs720).add(cs723).add(cs732).add(cs790)\
.add(hca742).add(hca745).add(Course('CompSci', '431G', '2'))

print(plan.get700CSCredits())
print(plan.getNonCSCredits())
print(plan.getCSGradCredits())
print(plan.isAcceptable())
print(plan)

#{
# output for the above plan of study
# 15
# 6
# 24
# True
# [HCA742, CompSci723, HCA745, CompSci720, CompSci790, CompSci535G, CompSci732, CompSci431G, CompSci715, CompSci481G]
# }
print("The below is the output for the 2nd test case")
plan = PlanOfStudy()
plan.add(cs431).add(cs481).add(cs535)\
.add(cs715).add(cs720).add(cs723).add(cs732)\
.add(hca740).add(hca742).add(hca745)
#{output for above plan of study
# 12
# 9
# 21
# False
# [CompSci535G, HCA742, HCA745, CompSci720, CompSci723, CompSci732, CompSci431G, HCA740, CompSci715, CompSci481G]
# }


print(plan.get700CSCredits())
print(plan.getNonCSCredits())
print(plan.getCSGradCredits())
print(plan.isAcceptable())
print(plan)