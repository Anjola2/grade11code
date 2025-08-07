#Anjola Kamoru
#ROller Coaster Ride
#6th August 2025
while True:
    position=int(input("Enter a number representing your position in line: "))
    cars=int(input("Enter the number of cars on the train: "))
    people=int(input("Enter the number of people a single car holds: "))

    no_of_people_per_ride= cars*people

    if(no_of_people_per_ride<position):
        print("no")
    else:
        print("yes")