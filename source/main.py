import sqlite3
import os

current_folder = os.path.dirname(__file__)
db_file = os.path.join(current_folder, "university.db")
sql_file = os.path.join(current_folder, "schema.sql")

def print_text_table(title, columns, data):
    """Prints neat text boxes in the terminal."""
    if not data:
        print(f"\n[No data found for {title}]")
        return

    print(f"\n{title}")
    print("-" * 65)
    
    header_string = ""
    for col in columns:
        header_string += f"{col:<22}"
    print(header_string)
    print("-" * 65)
    
    for row in data:
        row_string = ""
        for item in row:
            row_string += f"{str(item):<22}"
        print(row_string)
    print("-" * 65)

def main():
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    # Read and execute the SQL blueprint
    with open(sql_file, 'r') as file:
        cursor.executescript(file.read())

    # Interactive Menu
    while True:
        print("\n--- STUDENT REGISTRATION SYSTEM ---")
        print("1. Add a Course")
        print("2. Add a Student")
        print("3. View Database (The Retrieval Test)")
        print("0. Exit")
        
        choice = input("Select an option: ").strip()

        if choice == '1':
            course_name = input("Enter the course name (e.g., Computer Engineering): ")
            cursor.execute("INSERT INTO courses (course_name) VALUES (?)", (course_name,))
            connection.commit()
            print("Course successfully added!")

        elif choice == '2':
            # Display courses first so the user knows what ID to pick
            cursor.execute("SELECT * FROM courses")
            courses = cursor.fetchall()
            
            if not courses:
                print("Error: You must add a Course first before adding a Student!")
                continue
                
            print_text_table("Available Courses", ["Course ID", "Course Name"], courses)
            
            student_name = input("Enter the student's name: ")
            course_id = input("Enter the Course ID they belong to: ")
            
            cursor.execute("INSERT INTO students (name, enrolled_course_id) VALUES (?, ?)", (student_name, course_id))
            connection.commit()
            print(f"Student '{student_name}' successfully added!")

        elif choice == '3':
            # The Relational JOIN Query
            cursor.execute("""
                SELECT students.student_id, students.name, courses.course_name 
                FROM students 
                JOIN courses ON students.enrolled_course_id = courses.course_id
            """)
            joined_data = cursor.fetchall()
            print_text_table("DATABASE RECORD: Students and their Courses", ["Student ID", "Name", "Major"], joined_data)

        elif choice == '0':
            print("Closing the database. Your data is saved!")
            break
            
        else:
            print("Invalid option. Please try again.")

    connection.close()

if __name__ == "__main__":
    main()