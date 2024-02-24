# Accepting input details from user
city_flight = input("Enter the city of destination (e.g., Sheffield, Manchester, London, Scotland, Liverpool): ")
num_nights = int(input("Enter the number of night spent in hotel: "))
rental_days = int(input("Enter the number of Times of car rent: "))

# functions for computations of the total holiday details
def hotel_cost(num_nights):
    
    total1 = num_nights * 100
    
    return total1 

def plane_cost(city_flight):
    
    if city_flight == "Sheffield":
        return 250
    elif city_flight == "Manchester":
        return 300
    elif city_flight == "London":
        return 350
    elif city_flight == "Scotland":
        return 450
    elif city_flight == "Liverpool":
        return 150
    else:
        return 400

def car_rental(rental_days):
    total2 = rental_days * 100
    return total2

def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

# Intanciating the function
total_hotel_cost = hotel_cost(num_nights)
total_plane_cost = plane_cost(city_flight)
total_car_rental = car_rental(rental_days)
total_holiday_cost = holiday_cost(total_hotel_cost, total_plane_cost, total_car_rental)

# Printing the cost of holiday details
print("\nHoliday Details:")
print(f"City of Flight: {city_flight}")
print(f"Number of Nights in Hotel: {num_nights}")
print(f"Number of Rental Days for Car: {rental_days}")
print(f"Total Hotel Cost: £{total_hotel_cost}")
print(f"Total Plane Cost: £{total_plane_cost}")
print(f"Total Car Rental Cost: £{total_car_rental}")
print(f"Total Holiday Cost: £{total_holiday_cost}")