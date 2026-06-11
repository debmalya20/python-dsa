n=int(input("Enter the number="))# this is taking the input 
temp=n # we are storing the origns=al num in to an veriable
length=len(str(n)) # we are taking out the length of the input

total=0
while n>0: # this goes till the number is greater than zero
    last_digit=n%10 # we are taking out the last digit
    total=total+(last_digit**length) # we are multipying the power of the last digit
    n=n//10 # and removing the last digit because we have done the execution 
if temp==total: # is the temp is same as total then armstrong
    print(f"Your armstomr number is{total}")
else:
    print(f"Sorry {temp} not a armstrog number")