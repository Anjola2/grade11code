#Anjola Kamoru
#Deliv-e-droid
#7 Nov 2024

while True:
    number_of_packages_delivered=int(input("Enter the number of packages delivered: "))
    collision=int(input("Enter the number of collisons: "))

    total_points=(50*number_of_packages_delivered)-(10*collision)

    if (number_of_packages_delivered>collision):
        total_points=total_points+500
        print("Total points:",total_points,"points")

    else:
        print("Total points:",total_points,"points")