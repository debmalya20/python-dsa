n=int(input("Enter the number="))
temp=n
length=len(str(n))

total=0
while n>0:
    last_digit=n%10
    total=total+(last_digit**length)
    n=n//10
if temp==total:
    print(f"Your armstomr number is{total}")
else:
    print(f"Sorry {temp} not a armstrog number")