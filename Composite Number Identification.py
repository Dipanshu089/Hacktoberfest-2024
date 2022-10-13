print("To check if a number is Composite Number or not ; ")
n = int(input("Enter Number to check : "))
rec = 0
num = n//2+1
for i in range(2,num):
	check = n/i
	if (check).is_integer() == True:
		rec+=1
if rec>0:
	print('--The number entered is a Composite Number--')
else:
	print("--The number entered is NOT a Composite Number--")
