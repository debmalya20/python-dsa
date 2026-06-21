# this is known as head recurtion

# count=0
# def name():
#     global count
#     if count==4:
#         return
#     print("debmalya")
#     count +=1
#     name()
    
# name()

# this is tail recurtion

# count=0
# def name():
#     global count
#     if count==4:
#         return
#     count +=1
#     name()
    
#     print("DEB")

# name()

# print x=15 n=4 times

# def printnum(x,y):
#     if y==0:
#         return
#     print(x)
#     printnum(x,y-1)

# printnum(15,4)

#Q) Print 1 to n using recution

# def printnum(x,targer):
#     if x>targer:
#         return
#     print(x)
#     printnum(x+1,targer)
# printnum(1,12)


# sum of all eliment till n

def sums(i,target):
    while i == target:
        return i
    return i + sums(i+1,target)
print(sums(1,12))
