#Task 1:

done=False

while done==False:

    print('Welcome to the Hour to Minute Converter!')
    hours= input("Hours:")

    if '.' in hours:
        try:
            minutes= float(hours)*60.0
            print("Minutes:", minutes)
            done=True
        except ValueError:
            print("Please enter an integer or a decimal")
            continue

    elif '.' not in hours:
        try:
            minutes= int(hours)*60
            print("Minutes:", minutes)
            done=True
        except ValueError:
            print("Please enter an integer or a decimal")
            continue

#the rest is for extra practice
#Task 2:

print("Welcome to the hour to minute & minute to hour converter!")
possibleAnswers=['yes', 'Yes', 'YES', 'YEs', 'yEs', 'yeS', 'yES', 'yea', 'yup', 'yas']

done=False

while done==False:

    if input("Would you like to convert from hours to minutes?") in possibleAnswers:
        hours= input("Hours:")
        if '.' in hours: 
            try:
                minutes= float(hours)*60.0
                print("Minutes:", minutes)   
                done=True
            except ValueError:
                print("Please enter an integer or a decimal")
                continue
        elif '.' not in hours:
            try:
                minutes= int(hours)*60
                print("Minutes:", minutes)
                done=True
            except ValueError:
                print("Please enter an integer or a decimal")
                continue
    else:
        minutes= input("Minutes:")
        if '.' in minutes: 
            try:
                hours= float(minutes)/60.0
                print("Hours:", hours)
                done=True
            except ValueError:
                print("Please enter an integer or a decimal")
                continue
        elif '.' not in minutes:
            try:    
                hours= int(minutes)/60
                print("Hours:", hours)
                done=True
            except ValueError:
                print("Please enter an integer or a decimal")
                continue


#Task 3:
print("Welcome to letter counter!")
userInputtedWord=input("Word:")
print(len(userInputtedWord))