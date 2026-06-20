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

def printnum(x,y):
    if y==0:
        return
    print(x)
    printnum(x,y-1)
    
printnum(15,4)


