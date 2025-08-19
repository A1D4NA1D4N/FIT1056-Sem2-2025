


#Can be found on repository: https://github.com/A1D4NA1D4N/FIT1056-Sem2-2025

# pst2_main.py - The Persistent Application

import json
import datetime

DATA_FILE = "msms.json"
app_data = {} # This global dictionary will hold ALL our data.

# --- Core Persistence Engine ---
def load_data(path=DATA_FILE):
    """Loads all application data from a JSON file."""
    global app_data
    try:
        with open(path, 'r') as f:
            # TODO: Use json.load(f) to load the file's content into the global 'app_data' variable.
            app_data = json.load(f)
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("Data file not found. Initializing with default structure.")
        # TODO: If the file doesn't exist, initialize 'app_data' with a default dictionary.
        # It should have keys like: "students", "teachers", "attendance", "next_student_id", "next_teacher_id".
        # The lists should be empty and the IDs should start at 1.
        app_data = {
            "students": [],
            "teachers": [],
            "attendance": [],
            "next_student_id": 1,
            "next_teacher_id": 1
        }

def save_data(path=DATA_FILE):
    """Saves all application data to a JSON file."""
    # TODO: Open the file at 'path' in write mode ('w').
    # Use json.dump() to write the global 'app_data' dictionary to the file.
    # Use the 'indent=4' argument in json.dump() to make the file readable.
    with open(path, 'w') as f:
        json.dump(app_data, f, indent=4)
    print("Data saved successfully.")

# FRAGMENT 2.2

# --- Full CRUD for Core Data ---
# Note: We are now working with lists of dictionaries, not lists of objects.

def add_teacher(name, speciality):
    """Adds a teacher dictionary to the data store."""
    # TODO: Get the next teacher ID from app_data['next_teacher_id'].
    teacher_id = app_data['next_teacher_id']
    # TODO: Create a new teacher dictionary with 'id', 'name', and 'speciality' keys.
    new_teacher = {"id": teacher_id, "name": name, "speciality": speciality}
    # TODO: Append the new dictionary to the app_data['teachers'] list.
    app_data['teachers'].append(new_teacher)
    # TODO: Increment the 'next_teacher_id' in app_data.
    app_data['next_teacher_id'] += 1
    print(f"Core: Teacher '{name}' added.")

def update_teacher(teacher_id, **fields):
    """Finds a teacher by ID and updates their data with provided fields."""
    # TODO: Loop through the app_data['teachers'] list.
    for teacher in app_data['teachers']:
        # TODO: If a teacher's 'id' matches teacher_id:
        if teacher['id'] == teacher_id:
            # Use the .update() method on the teacher dictionary to apply the 'fields'.
            teacher.update(fields)
            print(f"Teacher {teacher_id} updated.")
            return
    print(f"Error: Teacher with ID {teacher_id} not found.")




def list_students():
    """Prints all students in the database."""
    print("\n--- Student List ---")
    if not student_db:
        print("No students in the system.")
        return
    # TODO: Loop through student_db. For each student, print their ID, name, and their enrolled_in list.
    for student in student_db:
        print(f"  ID: {student.id}, Name: {student.name}, Enrolled in: {student.enrolled_in}")

def list_teachers():
    """Prints all teachers in the database."""
    # TODO: Implement the logic to list all teachers, similar to list_students().
    print("\n--- Teacher List ---")
    for teacher in teacher_db:
        print(f"  ID: {teacher.id}, Name: {teacher.name}, Speciality: {teacher.speciality}")




def find_students(term):
    """Finds students by name."""
    print(f"\n--- Finding Students matching '{term}' ---")
    # TODO: Create an empty list to store results.
    # Loop through student_db. If the search 'term' (case-insensitive) is in the student's name,
    # add them to your results list.
    # After the loop, if the results list is empty, print "No match found."
    # Otherwise, print the details for each student in the results list.



    matching = []

    for student in student_db:
        if term in student.name:
            matching.append(student)
            for student in matching:
                print(f"  ID: {student.id}, Name: {student.name}, Enrolled in: {student.enrolled_in}")
                matching = [] # Reset the list to empty for future searches
    else:
        print("No match found")




def find_teachers(term):
    """Finds teachers by name or speciality."""
    # TODO: Implement this function similar to find_students, but check
    # for the term in BOTH the teacher's name AND their speciality.



    matching = []
    matching_specialty = []

    for teacher in teacher_db:
        if term in teacher.name:
            matching.append(teacher)
            for teacher in matching:
                print(f"  ID: {teacher.id}, Name: {teacher.name}, Enrolled in: {teacher.enrolled_in}")
                matching = [] # Reset the list to empty for future searches
    else:
        print("No match found for names")


    for teacher in teacher_db: # Seperates the output to specify the search attribute used
        if term in teacher.speciality:
            matching_specialty.append(teacher)
            for teacher in matching:
                print("Matches found for specialty \n", f"  ID: {teacher.id}, Name: {teacher.name}, Enrolled in: {teacher.enrolled_in}")
                matching_specialty = [] # Reset the list to empty for future searches
    else:
        print("No match found for specialty")



def remove_student(student_id):
    """Removes a student from the data store."""
    # TODO: Find the student dictionary in app_data['students'] with the matching ID.
    # If found, use the .remove() method on the list to delete it.
    # A list comprehension is a clean way to do this:
    # app_data['students'] = [s for s in app_data['students'] if s['id'] != student_id]




    for student in app_data['students']:
        if student_id == student:
            app_data.remove(student)
        else:
            print("student does not exist")

    
# TODO: Implement remove_teacher() and update_student() using the patterns above.

def remove_teacher(teacher_id):
    """Removes a teacher from the data store."""
   

    for teacher in app_data['teachers']:
        if teacher_id == teacher:
            app_data.remove(teacher)
        else:
            print("teacher does not exist")




# Fragment 2.3

# --- New Receptionist Features ---
def check_in(student_id, course_id, timestamp=None):
    """Records a student's attendance for a course."""
    if timestamp is None:
        # TODO: Get the current time as a string using datetime.datetime.now().isoformat()
        timestamp = datetime.datetime.now().isoformat()
    
    # TODO: Create a check-in record dictionary.
    # It should contain 'student_id', 'course_id', and 'timestamp'.
    check_in_record = {
        "student_id": student_id,
        "course_id": course_id,
        "timestamp": timestamp
    }
    # TODO: Append this new record to the app_data['attendance'] list.
    app_data['attendance'].append(check_in_record)
    print(f"Receptionist: Student {student_id} checked into {course_id}.")


# Feature added to list the exact time a student checked in.
    print(f"Time of Check in: ")
    print(datetime.datetime.now().isoformat())

    # Stored in a list for future reference

    check_in_time = []

    check_in_time.append([student_id, datetime.datetime.now().isoformat()])



def print_student_card(student_id):
    """Creates a text file badge for a student."""
    # TODO: Find the student dictionary in app_data['students'].
    student_to_print = None
    for s in app_data['students']:
        if s['id'] == student_id:
            student_to_print = s
            break
    
    if student_to_print:
        # TODO: Create a filename, e.g., f"{student_id}_card.txt".
        filename = f"{student_id}_card.txt"
        # TODO: Open the file in write mode ('w').
        with open(filename, 'w') as f:
            # Write the student's details to the file in a nice format.
            f.write("========================\n")
            f.write(f"  MUSIC SCHOOL ID BADGE\n")
            f.write("========================\n")
            f.write(f"ID: {student_to_print['id']}\n")
            f.write(f"Name: {student_to_print['name']}\n")
            f.write(f"Enrolled In: {', '.join(student_to_print.get('enrolled_in', []))}\n")
        print(f"Printed student card to {filename}.")
    else:
        print(f"Error: Could not print card, student {student_id} not found.")




        # additonal feature added to show current enrolles students if print card function fails to locate student ID
        print("Current enrolled students:\n")
        for student in app_data['students']:
            print(student)
        print("please ensure the student is within the enorlled list")




# Fragment 2.4

# --- Main Application Loop ---
def main():
    """Main function to run the MSMS application."""
    load_data() # Load all data from file at startup.

    while True:
        print("\n===== MSMS v2 (Persistent) =====")
        print("1. Check-in Student")
        print("2. Print Student Card")
        print("3. Update Teacher Info")
        print("4. Remove Student")
        print("q. Quit and Save")
        
        choice = input("Enter your choice: ")
        
        made_change = False # A flag to track if we need to save
        if choice == '1':
            # TODO: Get student_id and course_id from user, then call check_in().
            made_change = True
        elif choice == '2':
            # TODO: Get student_id, then call print_student_card().
            pass # No change made, so no save needed
        elif choice == '3':
            # TODO: Get teacher_id and new details, then call update_teacher().
            # Example: update_teacher(1, speciality="Advanced Piano")
            made_change = True
        elif choice == '4':
            # TODO: Get student_id, then call remove_student().
            made_change = True
        elif choice == '6': # added lines for search functions using "6" and "7" inputs
            search_term = input("Search for Student: ")
            find_students(search_term)
        elif choice == '7':
            search_term = input("Search for Teacher: ")
        elif choice =='8':
            list_students
        elif choice =='9':
            list_teachers
        elif choice.lower() == 'q':
            print("Saving final changes and exiting.")
            break
        else:
            print("Invalid choice.")
            
        if made_change:
            save_data() # Save the data immediately after any change.

    save_data() # One final save on exit.

# --- Program Start ---
if __name__ == "__main__":
    main()