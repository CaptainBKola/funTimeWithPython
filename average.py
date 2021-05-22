total = 0   # set total to zero will be use to set user inputs later
count = 0  # set the counting of inputs to zero
while (True): #keep asking users to enter a number till they enter done
    inp = input('Enter a number: ') # prompt users to enter a number
    if inp == 'done': #if user type done then average number is displayed
        break # break out from while loop
    try: # catch  error from the user when string other than done is enterred
        value = float(inp)
    except:
        print('Invalid input') #displays error message
        continue
    total = total + value #add all the numbers enterred
    count = count + 1 # count the numbers enterred and add it

average = total / count # finds average
print('Average:', average) #displays average
