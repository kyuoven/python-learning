cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# assigned cars variable to cars 100
print("There are", cars, "cars available.")
# assigned drivers variable to 30
print("There are only" , drivers , "drivers available.")
# assigned cars_not_driven variuable to calculate the amount
print("There will be" , cars_not_driven , "empty cars today.")
# assigned carpool_capacity variable to calculate the amount
print("We can transport" , carpool_capacity , "people today.")
# asssigned passengers variable to 90
print("We have", passengers , "to carpool today.")
# assigned average_passengers_per_car variable to calculate the amount
print("We need to put about", average_passengers_per_car , "in each car")