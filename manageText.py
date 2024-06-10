# creating a variable and storing the text 
# that we want to search 
search_text = "AnyCompany"

# creating a variable and storing the text 
# that we want to add 
replace_text = "replaced"

# Opening our text file in read only 
# mode using the open() function 

# make a new file that you want to edit in case you did not have any
# f1 = open("re-make/SampleFile.txt","w")
# f1.write("dummy,home")
# f1.close()

with open(r'car_fleet.csv', 'r') as file: 

	# Reading the content of the file 
	# using the read() function and storing 
	# them in a new variable 
	data = file.read() 

	# Searching and replacing the text 
	# using the replace() function 
	data = data.replace(search_text, replace_text) 

# Opening our text file in write only 
# mode to write the replaced content 
with open(r're-make/SampleFile.csv', 'w') as file: 

	# Writing the replaced data in our 
	# text file 
	file.write(data) 

# Printing Text replaced 
print("Text replaced") 
