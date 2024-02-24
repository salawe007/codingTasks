# inputting time for the games in munite
running_time = float(input("Enter time for running: "))
swimming_time = float(input("Enter time for swimming: "))
cycling_time = float(input("Enter time for cycling: "))

# calculating the total time of games

total_time = running_time  + swimming_time + cycling_time
print(f"Total Time is: {total_time}")

# Checking the actual award for each time
if total_time <= 100:
    print("Provincial Colours")
elif total_time <= 105:
    print("Provincial Half Colours")
elif total_time <= 110:
    print("Provincial Scroll")
else:
    print("No Award")
