import re

def course_code(code):
    check_course = r'^[A-Z]{2,3}\d{3}$'
    return bool(re.match(check_course, code))

print(course_code("TEC001"))  
print(course_code("AU006"))   
print(course_code("A10"))    


