n=int(input("Enter the number you want the palindrom of="))
num=n
reverse=0
while num>0:
    last_digit=num%10
    reverse=reverse*10+last_digit
    num=num//10
if reverse==n:
    print("This is palindrom")
else:
    print("Sorry its not a palindrom !")