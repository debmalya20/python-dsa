# nums=[1,2,7,6,4,3,5,9,8,10]
# l=0
# r=len(nums)-1

# while l<r:
#     nums[l],nums[r]=nums[r],nums[l]
#     l +=1
#     r -=1

# print(nums)

# using recurtion

# def reverse(arr,left, right):
#     if  left >=right:
#         return
#     arr [left],arr [right]=arr [right],arr [left]
#     reverse(arr, left+1, right-1)

# arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# reverse(arr,3,7)
# print(arr)
def reverse(arr,left,right):
    if left>=right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    reverse(arr,left+1,right-1)
arr=[1,2,3,4,5,6,7]
reverse(arr,2,6)
print(arr)