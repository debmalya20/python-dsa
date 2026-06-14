n=[1,2,3,4,4,3,2,5,6,7,8,2,3,4,2,3]
num=[1,2,3,4,5,6,7,8,9,1,11,222,33]

for i in num:
    count=0
    for j in n:
        if i==j:
            count+=1
    if count > 0:
        print(f"The {i} element was fount {count} times\n ")
    else:
        print(f"The{i} was not found in the list\n")