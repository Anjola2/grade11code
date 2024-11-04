#Anjola Kamoru
#Dusa And The Yobis
#4 Nov 2024

D=int(input("Dusa's Starting size: "))
yobis=0

while (D>yobis):
    yobis=int(input("Enter the size of the Yobis: "))
    if(D>yobis):
        D+=yobis
    else:
        break

print(D)
