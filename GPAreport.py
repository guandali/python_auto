from course import course
import sys
courses_list = []
MAX_COURSE_LIMIT = 6



print('Welcome to this GPA helper')
course_num = input('How many classes did you take? ')
if(course_num > MAX_COURSE_LIMIT or course_num < 1):
    print('NOT VALID COURSES')
    sys.exit()
for i in range(0, course_num):
    my_course_name = input('What was the name of this class? ')
    my_course_grade = input('What was your grade')
    my_course = course(my_course_name, my_course_grade)
    courses_list.append(my_course)
print(courses_list)