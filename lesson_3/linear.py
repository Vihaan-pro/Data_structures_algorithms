numbers = [7,100,3,4,5,6,111100,700,900,200,5500,600,234567890,987654321,400,600,156]
search = int(input("enter the number that you want search"))
# first method
if search in numbers:
    print("number exists")
else:
    print("number does not exist")

# second method
lenth = len(numbers)
for i in range (lenth):
    if numbers[i]== search:
        print("number found")

# third method
for i in numbers:
    if i == search :
        print ("number exists")
        


