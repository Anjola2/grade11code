#Anjola Kamoru
#Chili Pepper
#7 Nov 2024

num_of_chilis=int(input("Enter number of Chilis "))
SHU_values = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}
    

total_spiciness=0

for i in range(num_of_chilis):
    pepper = input("Enter name of pepper: ").capitalize()
    if pepper in SHU_values:
        total_spiciness += SHU_values[pepper]
    else:
        print(f"{pepper} is not in the list of available peppers.")

# Output the total spiciness of the chili
print("The total spiciness of the chili is:", total_spiciness, "SHU")



    
