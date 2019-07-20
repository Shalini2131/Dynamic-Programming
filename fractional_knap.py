def knapsack(value, weight, capacity):
    #index list with size of number of values   
    ind = list(range(len(value)))
    #ratio list containing ratio's of value & weight
    ratio = [v/w for v, w in zip(value, weight)]
    #sorting the index list based on the ratio's in non-decreasing order
    ind.sort(key=lambda i: ratio[i], reverse=True)
    #initializing maximum value to 0
    maxi= 0
    #looping over the index list
    for i in ind:
        #since the weight of the item should be less than the capacity.. check condition
        if(weight[i]<=capacity):
            maxi+=value[i];
            #after adding the weight of item subtracting it from the capacity
            capacity-=weight[i]
        else:
            #if the weight is greater then we add the fractional weight of item inorder to have maximum value in given capacity
            maxi+=value[i]*capacity/weight[i]
            break
    return maxi
#inputting the size i.e number of items
n=int(input('Enter no:of items :'))
#reading values given by user in list "value"
value=[int(i) for i in input('Enter values :').split()]
#reading weights given by user in list "weight"
weight=[int(i) for i in input('Enter weights :').split()]
#inputting the capacity of the knapsack
capacity=int(input('Enter Capacity : '))
#storing the maximum value in "max" variable
maxi=knapsack(value,weight,capacity)
#printing the result
print('maximum value is ',maxi)
