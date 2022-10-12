print("Enter Text to swap case for : ")
s = list(input())
for i in range(len(s)):
	if(s[i] == s[i].upper()):
		s[i] = s[i].lower()
	elif(s[i] == s[i].lower()):
		s[i] = s[i].upper()
print("Case Swaped text is : ")
for j in range(len(s)):
	print(s[j] ,end="")
