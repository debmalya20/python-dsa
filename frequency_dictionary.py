num=[1,2,3,4,5,1,2,3,4,5,6,7,8,8,9]
frequency=dict()
for i in range(0,len(num)):
    if num[i] in frequency:
        frequency[num[i]]+=1
    else:
        frequency[num[i]]=1
print(frequency)