# Armstrong Number is a number that equals the sum of its digits, each raised to a power of number of digits it has

num1 = int(input())              # the number taken input 
temp = num1                         # copy of the number taken input 
sum = 0                          # sum of the digits to be calculated in 
num_len = len(str(temp))            # number of digits of the number entered
for i in range(num_len):
    d = num1% 10                 # digit recieved as remainder
    sum+= d**(num_len)           # all digits raised to the power of number of digits are added together
    num1 = num1 // 10 
if sum == temp :
    print("the number is armstrong ")
else:
    print("the number is not armstrong")