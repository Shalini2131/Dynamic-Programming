def knapsack(value, weight, capacity):
    ind = list(range(len(value)))
    ratio = [v/w for v, w in zip(value, weight)]
    ind.sort(key=lambda i: ratio[i], reverse=True)
    maxi= 0
    for i in ind:
        if(weight[i]<=capacity):
            maxi+=value[i];
            capacity-=weight[i]
        else:
            maxi+=value[i]*capacity/weight[i]
            break
    return maxi
n=int(input('Enter no:of items :'))
value=[int(i) for i in input('Enter values :').split()]
weight=[int(i) for i in input('Enter weights :').split()]
capacity=int(input('Enter Capacity : '))
maxi=knapsack(value,weight,capacity)
print('maxiimum value is ',maxi)