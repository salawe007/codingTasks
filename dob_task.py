# creating a function to read from Copy of DOB.txt
def dob_data(birth_info):
    names = []
    birthdates = []
    with open("Copy of DOB.txt", 'r') as file:
        for line in file:
            name = line.strip().split()
            birthdate = line.strip().split()
            full_names = name[0]+" "+name[1]
            full_birth = birthdate[2]+" "+birthdate[3]+" "+birthdate[4]
            names.append(full_names)
            birthdates.append(full_birth)
    return names, birthdates

# a function to display the names and birthdates
def print_dob_data(names, birthdates):
    print("Name")
    for name in names:
        print(name)
    print("\nBirthdate")
    for birthdate in birthdates:
        print(birthdate)

# calling the functions
if __name__ == "__main__":
    birth_info = "Copy of DOB.txt"
    names, birthdates = dob_data(birth_info)
    print_dob_data(names, birthdates)
 