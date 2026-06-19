count=0
def name():
    global count
    if count==4:
        return
    name()
    print("DEB")

name()
