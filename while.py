# initializinf a list variable to hold the numbers
numbers = []

# a loop that will continue requesting a user to enter a number
while True:
    user = input("Enter a number: ")
    if  user == "-1":
       break
    else:
        numbers.append(float(user))

# calculating the total and average        
total = sum(numbers)
average = total/(len(numbers))

print(f"the average of the numbers is: {average:.2f}")
        
        
       
   
    
    
        
    
    