#Anjola Kamoru
#Special Event
#19 Nov 2024

num_of_people=int(input("Enter number of people attending event: "))
counts=[0,0,0,0,0]

for i in range(num_of_people):
    day=input("Availability: ").upper()
    if len(day) != 5 or not all(c in "Y." for c in day):
        print("Invalid input. Please enter exactly 5 characters using Y/.")
        continue
    for i in range(5):
        if day[i] == "Y":
            counts[i]+=1

max_count = max(counts)
best_days = [i + 1 for i, count in enumerate(counts) if count == max_count]

print(",".join(map(str,best_days)))

