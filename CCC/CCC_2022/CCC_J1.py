#Anjola Kamoru
#Cupcake Party
#19 Nov 2024

try:
    regular=int(input("Enter number of regular boxes of cupcakes: "))
    small=int(input("Enter number of small boxes of cupcakes: "))
except ValueError:
    print("Invalid Input. Please enter a valid integer.")
    exit()  
total=(regular*8)+(small*3)

remainder=total-28
print(remainder)

