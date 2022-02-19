import os
import os.path

Restart = True
while Restart == True: 
	Introduction = print("Hello! Let's create a file for your profile!\n Please select a name for your profile and save the file!")
	fileName = input("What will you name your file?: ")
	print(fileName)

	location = input("Where would you like to save your file?\n Please enter the desired directory location: ")
	print(location)
	filePath = os.path.join(location, fileName)

	check = os.path.isdir(location)
	print(check)

	if check == False:
		option = input("That file location is not valid. Would you like to try again?: \n")
		if option == "yes":
			
			continue
		if option == "no":
			break	

	if check == True:
		userName = input("What is your name?: ")
		address = input("What is your address?: ")
		phone = input("What is your phone number?: ")
		break

	else:
		break
print("Ok!")

try:
	with open(filePath, 'w') as file_object: #create a new file
		data = (userName + ", " +address + "," +phone)
		file_object.write(data) #write to file
except (Exception):
    print("Error creating/writing to new file.")
    quit()

try:
    with open(filePath) as file_object:
        print("Today we created a new file, " + fileName +
              ", and we added the following information to the file: ")
        print(file_object.read())
except Exception:
    print("Error reading file.")
    quit()



#Reference: some code obtained from 
# https://stackoverflow.com/questions/70553437/i-need-to-be-able-to-create-a-new-file-to-a-specific-directory-and-then-write-to