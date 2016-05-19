from course import course
import sys
courses_list = []
MAX_COURSE_LIMIT = 6

def getAvg(courses_list, course_num):
    sum = 0
    for i in range(0, course_num):
        sum = courses_list[i].getCourseGrade()+ sum
        avg = sum/course_num
    return avg
def printReport(courses_list, average, course_num):
    print('REPORT CARD:\n')
    print('\n')
    for i in range(0, course_num):
        print(courses_list[i].getCourseName(), '  -  ', courses_list[i].getCourseGrade())
    print('\n')
    print('Overall GPA –  ', average)

print('Welcome to this GPA helper')
course_num = int(input('How many classes did you take? '))
if(course_num > MAX_COURSE_LIMIT or course_num < 1):
    print('NOT VALID COURSES')
    sys.exit()
for i in range(0, course_num):
    my_course_name = input('What was the name of this class? ')
    my_course_grade = int(input('What was your grade'))
    my_course = course(my_course_name, my_course_grade)
    courses_list.append(my_course)

#print(courses_list)
average = getAvg(courses_list,course_num)
#print('The avg is :', average)
printReport(courses_list, average, course_num)
