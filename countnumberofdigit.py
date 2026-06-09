n=int(input("Enter number="))
num=n
count=0
while num >0:
    num=num//10
    count+=1
print("The total numbers are",count)
