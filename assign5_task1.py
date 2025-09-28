student_marks = {
    "Rutuja": 85,
    "Aditya": 90,
    "Sakshi": 78,
    "gauri": 92
}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print(f"Sorry, no record found for '{name}'.")