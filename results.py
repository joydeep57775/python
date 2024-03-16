# using Function:
# def calculate_division(marks):
#     total_marks = sum(marks)
#     percentage = (total_marks/600)*100
#     if percentage>= 60:
#         return "1st Div"
#     elif percentage >= 45:
#         return "2nd Div"
#     elif percentage>=30:
#         return "3rd Div"
#     else:
#         return "Fail"
# def input_marks():
#     marks = []
#     print("Enter marks for 6 subjects: ")
#     for i in range(6):
#         subject_mark = float(input(f"Enter marks for subjects {i+1}: "))
#         marks.append(subject_mark)
#     return marks
# ram_marks = input_marks()
# ram_division = calculate_division(ram_marks)
# print("Ram's divison is: ", ram_division)

# Input marks of Ram
ram_marks = []

for i in range(6):
    marks = float(input(f"Enter the marks of Ram in subject {i+1}: "))
    ram_marks.append(marks)

total_marks = sum(ram_marks)

print("Total Marks Obtained by Ram:", total_marks)

if total_marks >= 60 * 6:
    division = "First Division"
elif total_marks >= 45 * 6:
    division = "Second Division"
elif total_marks >= 30 * 6:
    division = "Third Division"
else:
    division = "Fail"

print("Division of Ram:", division)