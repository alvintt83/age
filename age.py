driving = input('Have you ever driven a car before? ')
if driving != 'Yes' and driving != 'No':
	print("Either Yes or No")
	raise SystemExit
age = input('Enter your age: ')
age = int(age)
if driving == 'Yes':
    if age >= 18:
        print('You pass the test.')
    else:
        print('Oops, How come you have driven a car before?')
elif driving == 'No':
    if age >=18:
        print("You are eligible to obtain a Driving License.")  
    else:
    	print("You're not old enough to get a Drive's License. ")