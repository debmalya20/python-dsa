nums=[1,2,7,6,4,3,5,9,8,10]
l=0
r=len(nums)-1

while l<r:
    nums[l],nums[r]=nums[r],nums[l]
    l +=1
    r -=1

print(nums)
