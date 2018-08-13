def is_happy(number):
    # Parse int to list
    number_list = [int(d) for d in str(number)]

    #Create empty list for squares
    squares_list = []

    #Iterate through number list and add squares to square_list
    for d in number_list:
        squares_list.append(d**2)

    #Add digits together
    total = 0
    for i in squares_list:
        total += i

    #Display current total
    print(total)

    #Check if happy, unhappy or in progress
    if(total == 1):
        return True
    elif(total == 4):
        return False
    else:
        return is_happy(total)

#Get number of Happy numbers to be found
happy_count = input('How many happy numbers do you want to find? ')

if(happy_count.isdigit() == False):
    print('Entry was not a number')
else:
    #Lists
    happy_list = []
    unhappy_list = []
    i = 0
    #iterate through all numbers to see if happy
    while len(happy_list) < int(happy_count):
        i+=1
        if(is_happy(i) == False):
            unhappy_list.append(i)
        elif(is_happy(i) == True):
            happy_list.append(i)
        else:
            print("Error")
            continue
        print('Found happy numbers: '+ str(happy_list))
        print('Found unhappy numbers: '+ str(unhappy_list))
