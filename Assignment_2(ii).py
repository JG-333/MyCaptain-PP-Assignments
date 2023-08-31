# To print positive numbers in a list

l = []
l = [int(item) for item in input("Enter list items separated by a comma(,).\n ").split(",")]
c = 0
print("Positive numbers are...")
while(c < len(l)):
	if l[c] >= 0:
		print(l[c], end = "\n")
	c += 1

