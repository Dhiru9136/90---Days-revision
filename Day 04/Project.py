# Student Management System 

# Menu:

# ===== Student Management =====
# 1. Add Student
# 2. View Students
# 3. Exit

# Rules

# Data list mein store karo.
# File handling abhi mat use karna.
# Functions use karna.

student = []

# Function to add student
def add_student():
    name = input("Enter Student Name: ")
    student.append(name)
    print("Student Added Successfully!")

# Function to view students
def view_students():
    if len(student) == 0:
        print("No students found.")
    else:
        print("\nStudent List:")
        for i in range(len(student)):
            print(f"{i + 1}. {student[i]}")

# Main Menu
while True:
    print("\n===== Student Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    enter = int(input("Select the option: "))

    if enter == 1:
        add_student()

    elif enter == 2:
        view_students()

    elif enter == 3:
        print("Thank You!")
        break

    else:
        print("Invalid Option!")