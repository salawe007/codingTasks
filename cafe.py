
# Create a list of items in the menu
menu = ["burger", "coffee", "dognut", "chips", "pizza"]

# Creating a dictionary to store the stock value for each item
stock = {"burger": 100, "coffee": 50, "dognut": 30, "chips": 20, "pizza":25}

# Creating a dictionary to store the price for each item
price = {"burger": 3.6, "coffee": 1.69, "dognut": 4.9, "chips": 2.3, "pizza":10.5}

# Calculating the total stock worth in the cafe
total_worth = 0
for items in menu:
    item_value = stock[items] * price[items]
    total_worth += item_value

# Print the result
print("Total stock worth in the cafe: £{:.2f}".format(total_worth))
    
