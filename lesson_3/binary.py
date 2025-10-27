numbers = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000]
search = int(input("enter the number that you want search"))
low = 0
high = len(numbers)-1
while low <= high:
    mid = (low + high)// 2
    if numbers [mid]== search:
        print("number is found")

        break
    elif numbers [mid]< search:
        low = mid + 1
    else :
        high = mid - 1

# for binary search orderd data and leanar no 
# lenear searches 1 by 1 and binary divides the list until it reaches the number
# lenaer search faster in small data but slower in large data and oposite for binary