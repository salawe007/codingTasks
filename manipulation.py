str_manip = input("Enter a sentence: ")

# calculating the lenght of the sentence
print(len(str_manip))

# finding the last letter in the string
print(str_manip[-1])

# replacing the ocuring letter "e" with "@""
print(str_manip.replace("e", "@"))

# printing the last three letter in a string backwards

print(str_manip[-3:][::-1])

#  five-letter word that is made up of the first three characters and the last two characters in str_manip

print(str_manip[:3]+str_manip[-2:])