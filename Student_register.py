def students():
    # Ask user for the number of students registering
    num_students = int(input("How many students are registering? "))

    # Open the file in write mode
    with open("reg_form.txt", "w") as file:
        # Loop through each student
        for i in range(num_students):
            # Ask for student ID
            student_id = input(f"Enter student {i + 1} id number: ")
            
            # Write student ID to the file
            file.write(student_id + '\n')
            
            # Adding a dotted line after each ID
            file.write("." * 20 + "\n")

    print("Registration successful")

if __name__ == "__main__":
    students()
    
