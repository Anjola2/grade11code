#Anjola Kamoru
#Donut Shop
#6th August 2025

no_of_donuts_available= int(input("Number of donuts available when the shop first opens: "))
if (no_of_donuts_available<0):
    print("Input a positive integer.")

events=int(input("Number of events throughout the day: "))

for i in range(events):
    bake_sold=input("input plus if donut has been baked and minus if sold: ")
    number_baked_sold=int(input("Enter number of donuts baked or sold: "))
    if bake_sold=="+":
        no_of_donuts_available+=number_baked_sold
    elif bake_sold=="-":
        no_of_donuts_available-=number_baked_sold
    else:
        print("Input + or -")

print("Number of donuts left at closing: {}".format(no_of_donuts_available))
    

