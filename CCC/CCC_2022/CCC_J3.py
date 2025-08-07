#Anjola Kamoru
#Harp Tuning
#19 Nov 2024



# result = []
# start_index = 0
# for i in range(len(tuning)):
#     if tuning[i].isdigit():
#         if start_index < i:
#              result.append(tuning[start_index:i-1])
#         start_index = i + 1 
# if start_index < len(tuning):
#     result.append(tuning[start_index:])
           
# print(result)

#user input
tuning=input("Enter tuning instructions: ")

#list for storing multiple paryts of i
alpha = []
num=[]
symbol=[]

#empty strings to store sections of input
temp_alpha=""
temp_num=""
temp_symbol=""

#looping through every character 
for i in range(len(tuning)):
    #Checking if the character is an alphabet
    if tuning[i].isalpha():
        temp_alpha+=tuning[i]# adding alphabet to a string
    #Checking if character is + or -
    elif tuning[i] in "+-":
        alpha.append(temp_alpha)#appending the alphabet variable to an alphabet list
        temp_symbol+=tuning[i] #putting symbol into a string
        temp_alpha="" #emptying the alphabet string
        symbol.append(temp_symbol) #appending symbol variable to a symbol list
        temp_symbol=""#emptying symbol veriable
    # checking if character is a number    
    elif tuning[i].isdigit():
        temp_num+=tuning[i] #adding number to a number variable

    #checking if character is an alphabet and the previous character is a number or if we are at the end of the input so we can know to append the number variable to a number list and reset number variable.
    if tuning[i].isalpha() and tuning[i-1].isdigit() or i==len(tuning)-1:
        #checking if number string is not empty
        if temp_num:
            num.append(temp_num) #appending number string to number list
            temp_num=""#emptying number string/variable
        

#looping to print coresspoding index for all three list
for check in range(len(symbol)):
    #checking if symbol is + or - and printing appropriate output based on that.
    if symbol[check]=="+":
        print(alpha[check],"tighten",num[check])
    if symbol[check]=="-":
        print(alpha[check],"loosen",num[check])



