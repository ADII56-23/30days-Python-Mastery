import sqlite3

# ---------------- DATABASE MANAGER ----------------
class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()
        self.create_table

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll INTEGER PRIMARY KEY,
            name TEXT,
            math INTEGER,
            science INTEGER,
            english INTEGER,
            total INTEGER,
            percentage REAL,
            grade TEXT
        )
        """)
        self.conn.commit()

    def insert_student(self, data):
        self.cursor.execute("""
        INSERT INTO students VALUES (?,?,?,?,?,?,?,?)
        """, data)
        self.conn.commit()

    def fetch_all(self):
        return self.cursor.execute("SELECT * FROM students").fetchall()

    def fetch_one(self, roll):
        return self.cursor.execute(
            "SELECT * FROM students WHERE roll=?", (roll,)
        ).fetchone()


# --- STUDENT CLASS---
class Student:
    def __init__(self, roll, name, math, science, english):
        self.roll = roll
        self.name = name
        self.math = math
        self.science = science
        self.english = english

    def calculate_result(self):
        total = self.math + self.science + self.english
        percentage = total / 3

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "Fail"

        return total, percentage, grade


# --------- MAIN PROGRAM ----------------
def main():
    db = DatabaseManager()

    while True:
        print("\n--- STUDENT RESULT MANAGEMENT ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            roll = int(input("Roll No: "))
            name = input("Name: ")
            math = int(input("Math Marks: "))
            science = int(input("Science Marks: "))
            english = int(input("English Marks: "))

            student = Student(roll, name, math, science, english)
            total, percentage, grade = student.calculate_result()

            db.insert_student(
                (roll, name, math, science, english, total, percentage, grade)
            )
            print("✅ Student Added Successfully")

        elif choice == "2":
            students = db.fetch_all()
            for s in students:
                print(s)

        elif choice == "3":
            roll = int(input("Enter Roll No: "))
            student = db.fetch_one(roll)
            if student:
                print(student)
            else:
                print("❌ Student Not Found")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("❌ Invalid Choice")


if __name__ == "__main__":
    main()
