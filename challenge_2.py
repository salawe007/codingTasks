# accepting input from user
string_fav = input("Enter the name of your favourite restaurant: ")
int_fav = int(input("Enter your favourite number: "))

# printing out the output inputed by the user
print(f"The name of my favourite resturant is {string_fav}")
print(f"My favourite number is {int_fav}")

casting_string_fav = int(string_fav)
print(casting_string_fav)

"""
Error message: invalid literal for int function that is, ValueError

explanation: String of characters can not be cast into interger because they are not values 
"""
