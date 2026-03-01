import os
import time
import sys

# ================= DATA =================

students = []


# ================= TOOLS =================

def clear():
    os.system("clear")


def type_text(text, speed=0.05):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def anim_input(text, speed=0.05):
    type_text(text, speed)
    return input(": ").strip()


# ================= FEATURES =================

def add_students():
    clear()

    type_text("=== ADD STUDENT ===")

    name = anim_input("Enter Name:")

    # ID input (with duplicate check)
    while True:
        id_num = anim_input("Enter ID number:")

        if id_num in [s["id"] for s in students]:
            type_text("ID already exists. Try again.", 0.03)
        else:
            break

    section = anim_input("Enter Section:")

    # Number of subjects
    while True:
        try:
            count = int(anim_input("Number of subjects:"))
            break
        except ValueError:
            type_text("Please enter a valid number.", 0.03)

    grades = []
    total = 0

    # Grades
    for i in range(count):
        while True:
            try:
                grade = float(anim_input(f"Enter grade {i+1}:"))
                grades.append(grade)
                total += grade
                break
            except ValueError:
                type_text("Invalid grade. Try again.", 0.03)

    average = total / len(grades)

    type_text(f"Average: {average:.2f}")

    student = {
        "name": name,
        "id": id_num,
        "section": section,
        "grades": grades,
        "average": average
    }

    students.append(student)

    type_text("Student added successfully!")
    input("Press Enter to continue...")


def display_students():
    clear()

    type_text("=== STUDENT LIST ===")

    if not students:
        type_text("No students found.")
        input("Press Enter...")
        return

    for i, student in enumerate(students, 1):
        type_text(f"--- Student {i} ---")
        type_text("Name: " + student["name"])
        type_text("ID: " + student["id"])
        type_text("Section: " + student["section"])
        type_text("Average: " + f"{student['average']:.2f}")
        print()

    input("Press Enter to continue...")


# ================= UI =================

def show_menu():
    clear()

    menu = [
        "======================",
        "   STUDENT SYSTEM",
        "======================",
        "1. Add Student",
        "2. Display Students",
        "3. Exit",
        "======================"
    ]

    for line in menu:
        type_text(line, 0.03)


# ================= MAIN LOOP =================

def main():

    while True:

        show_menu()

        choice = anim_input("Choose 1, 2, or 3:")

        match choice:

            case "1":
                add_students()

            case "2":
                display_students()

            case "3":
                clear()
                type_text("Program terminated.")
                break

            case _:
                type_text("Invalid choice.", 0.03)
                time.sleep(1)


# ================= RUN =================


main()
