#Anjola Kamoru
#Fergusonball Ratings
#19 Nov 2024
try:
    num_of_players=int(input("Enter total number of players on team: "))
except ValueError:
    print("Invalid Input. Try again")
    exit()
ratings=[]
count=0
for i in range(num_of_players):
    try:
        points = int(input(f"Enter the number of points scored by player {i + 1}: "))
        fouls = int(input(f"Enter the number of fouls committed by player {i + 1}: "))
    except ValueError:
        print("Invalid Input. Please enter valid integers for points and fouls.")
        exit()
    
    stars=(points*5)-(fouls*3)
    ratings.append(stars)

for i in range(num_of_players):
    if ratings[i]>40:
        count+=1
if count==num_of_players:
    print(f"{count}+")
else:
    print(count)