# n=int(input("Enter the number you want the palindrom of="))
# num=n
# reverse=0
# while num>0:
#     last_digit=num%10
#     reverse=reverse*10+last_digit
#     num=num//10
# if reverse==n:
#     print("This is palindrom")
# else:
#     print("Sorry its not a palindrom !")


# using pointer
def is_palinderom(s):
    length = len(s)
    left = 0
    right = length - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


s = "alash"
print(is_palinderom(s))
