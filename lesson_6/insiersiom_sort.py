n = [12,34,2,5,7]

for i in range(0,len(n)):     # the outer loop to travers from 1st item to last item of the list
    min = 10000000 #assume that this is the smallest number
    min_loc = -1 # location of the smallest number
    for j in range(i,len(n)): # check every number after curent position to find the smallest number
        if min>n[j]: # compare min n with other number if a number is smaller than min number 
            min = n[j] #update min number
            min_loc  = j # update the position of the min number
            n[i],n[j] = n[j],n[i] # swap the nuber and put the samallest number in its position

print(n)