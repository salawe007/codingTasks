# Defining the maximum number of stars
max_number_stars = 5

# Printing the pattern
for i in range(1, max_number_stars * 2):
    if i <= max_number_stars:
        print('*' * i)
    else:
        print('*' * (max_number_stars * 2 - i))
