#Task 24.2
#Task name : Holiday.py
#Written by: Hamza Asad
#Date: 2020/03/17


#Define the term for hotel_cost and make a varaible called num_of_nights
def hotel_cost(num_of_nights):
    #Make a variable called total and Num_of_nights * 1600 which is price per night
    total = num_of_nights * 1600
    #Return the total 
    return total

#Define the plane_cost and make the variable city
def plane_cost(city):
    #Check if the user chooses the city durban then use the price below
    if city.lower() == "durban":
        #This is where we store the price
        price = 1200
        #Return price now
        return price

    #Check if the user enters the city cape town
    elif city.lower() == "cape town":
        #This is where we store the price if the user chooses cape town
        price = 2000
        #return price
        return price
    
    #Check if the user chooses johannesburg city 
    elif city.lower() == "johannesburg":
        #store the price for getting a ticket to johannesburg
        price = 850
        #Return price
        return price

    #Check if the user chooses the City mauritius
    elif city.lower() == "mauritius":
        #Store the price below
        price = 3000
        #Return price
        return price

    #Check if the user chooses the city zimbabwe and print the prices for it below
    elif city.lower() == "zimbabwe":
        #store the price here
        price = 1800
        #Return price
        return price

    #Use a Else statement if the user chose something other than these optins
    else:
        #print a statement
        print("Flights to this area are unavailable.")

#Ask the user for their name
name = input("Please enter your name: ")

#Welcome them
print(f"Welcome {name}")

#Define car_rental and make the variable num_of_days
def car_rental(num_of_days):
    #Store the price for each day here
    cost_per_day = 400
    #This is the rental price for how many days times the cost per day
    rental_price = int(cost_per_day * num_of_days)
    #Retun rental price
    return rental_price

#Deine holiday_cost, this is for the full holiday cost
def holiday_cost(hotel_cost, plane_cost, car_rental):
    #This is the addition of all the things that they have to pay for which is car rental, hotel, etc...
    full_cost = hotel_cost(num_of_nights) + plane_cost(city) + car_rental(num_of_days)
    #Retuen full cost
    return full_cost

#This is to make it more presentable
print("="*10)
#Let the user knoew where the flights are available to
print("Flights are availabe to: \n> Durban < \n> Cape Town < \n> Johannesburg < \n> Mauritius < \n> Zimbabwe <")
#Print empty line for space
print()

#Ask the user to enter their destination
city = input("Please enter your destination: ")

#Skip a line
print()
#Ask the user how many nights will they be spending
num_of_nights = int(input("How many nights will you spending in the hotel: "))

#Skip a line
print()
#Request an answer from the user for how long they want to rent the car
num_of_days = int(input("For how many days would you like to rent a car: "))

#Skip a line
print()
#Add all of the answers from above and make it into a total which will show the total price
total_cost = hotel_cost(num_of_nights) + plane_cost(city) + car_rental(num_of_days)

#This is to make it presentable
print("=-"*40)
#Print a message and notify the user about the price at the hotel for how many days they chose 
print(f"The total amount for {num_of_nights} nights at the hotel will cost you: R{hotel_cost(num_of_nights)}")

#Print a message and print out their price to whichever city the user inputs 
print(f"The total price for your ticket to {city} will be: R{plane_cost(city)}")

#Print a message for the user to notify him about the price for how many days he chooses to rent the car
print(f"Your car rental Cost for {num_of_days} days is going to be: R{car_rental(num_of_days)}")

#Print out a message and show the user the total amount including hotels, the city they chose and car rental prices.
print(f"The total amount for this holiday is going to cost you: R{total_cost}")

#This is to make it more presentable
print("=-"*40)
#Print out a message to make the user feel special and make them smile ;)
print("Enjoy your holiday \nThank you for booking with us.")
#Skip a line
print()
#Print out a message
print("We hope to see you soon!")

