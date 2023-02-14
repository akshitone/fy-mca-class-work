marks_of_three_subjects = list(map(float, input(
    "Enter a student's assessment marks (separated by comma):").split(",")))

lab_exercise, report, final_examination = marks_of_three_subjects

final_marks = (lab_exercise * 0.2) + (report * 0.4) + (final_examination * 0.4)

student_grade_letter = ""

if final_marks >= 85 and final_marks <= 100:
    student_grade_letter = "HD"
elif final_marks >= 75:
    student_grade_letter = "D"
elif final_marks >= 65:
    student_grade_letter = "C"
elif final_marks >= 50:
    student_grade_letter = "P"
elif final_marks >= 45:
    if 0 in marks_of_three_subjects:
        student_grade_letter = "F"
    else:
        if lab_exercise <= 40 or report <= 40:
            student_grade_letter = "SA"
        elif final_examination <= 40:
            student_grade_letter = "SE"
        else:
            student_grade_letter = "F"
else:
    if marks_of_three_subjects.count(0) >= 2:
        student_grade_letter = "AF"
    else:
        student_grade_letter = "F"


print(final_marks)
print(student_grade_letter)

'''

AVOIDING FLAG
IN OPERATOR

isFail = False

for mark in marks_of_three_subjects:
    if mark == 0:
        isFail = True

if isFail:
    student_grade_letter = "F"
    
'''


'''

COUNT NUMBER OF OCCURANCE INTO THE LIST

counter = 0
for mark in marks_of_three_subjects:
    if mark == 0:
        counter += 1
'''


'''

PACKING - UNPACKING 
LIST INDEXING

lab_exercise = marks_of_three_subjects[0]
report = marks_of_three_subjects[1]
final_examination = marks_of_three_subjects[2]
'''


'''

STRING SPLIT
CONVERT STRING TO FLOAT DATA TYPE
APPENDING VALUES TO THE LIST

marks_of_three_subjects = marks_of_three_subjects.split(",")

converted_marks = list()

for mark in marks_of_three_subjects:
    result = float(mark)
    converted_marks.append(result)

# print(marks_of_three_subjects)
print(converted_marks)
'''


'''

TAKING INPUT FROM THE USER AND CONVERTED INTO THE FLOAT DATA TYPE

lab_exercise = float(input("Enter lab exercise marks:"))
report = float(input("Enter report marks:"))
final_examination = float(input("Enter final examination marks:"))

print(lab_exercise, type(lab_exercise))
print(report, type(report))
print(final_examination, type(final_examination))
'''
