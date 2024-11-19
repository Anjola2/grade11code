#Anjola Kamoru
#Bronze Counr 
#4 Nov 2024

n=int(input("Enter the number of participants: "))

scores=[]
for i in range(n):
    score=int(input("Enter the score of participant: "))
    scores.append(score)

final=sorted(set(scores))
bronze_score=final[-3]
bronze_count= scores.count(bronze_score)

print(bronze_score, bronze_count)



