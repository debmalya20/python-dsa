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

count=0
def name():
    global count
    if count==4:
        return
    count +=1
    name()
    
    print("DEB")

name()


