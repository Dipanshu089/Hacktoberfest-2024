class Emp(Person):

def Print(self):
	print("Emp class called")
	
Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()
