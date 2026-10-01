# Student Record Management using File Handling

filename = "students.txt"

# Add student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
course = input("Enter course: ")
marks = input("Enter marks: ")

with open(filename, "a") as file:
    file.write(f"{roll_no}, {name}, {course}, {marks}\n")

print("\nStudent record added successfully!")

# Display all student records
print("\n--- Student Records ---")

with open(filename, "r") as file:
    for record in file:
        print(record.strip())

# Search student by roll number
search_roll = input("\nEnter roll number to search: ")

found = False

with open(filename, "r") as file:
    for record in file:
        data = record.strip().split(", ")

        if data[0] == search_roll:
            print("\nStudent Found!")
            print("Roll No:", data[0])
            print("Name:", data[1])
            print("Course:", data[2])
            print("Marks:", data[3])
            found = True
            break

if not found:
    print("Student not found!")
