# def threeSum(nums: list[int]) -> list[list[int]]:
#         res = []

#         if len(nums) == 3 and sum(nums) == 0:
#             res.append(nums)
#             return res
        
#         if len(nums) == 3 and sum(nums) != 0:
#             return res
        
#         for i in range(len(nums)):
#             first = 0
#             second = 1

#             while not second >= len(nums):
#                 arr = sorted([nums[i], nums[first], nums[second]])
#                 print(sum(arr), arr)
#                 if sum(arr) == 0 and arr not in res:
#                     res.append(arr)
#                     print(res)
#                 first += 1
#                 second += 1
#         return res

# print(threeSum([-100,-70,-60,110,120,130,160]))


from typing import List

def threeSum( nums: List ):
    nums.sort()
    res = []
    print(f"Sorted {nums}")

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = len(nums) - 1

        while left < right:
            print(nums[i], nums[left], nums[right])
            total = nums[i] + nums[left] + nums[right]

            if total > 0:
                right -= 1
            
            elif total < 0:
                left += 1
            
            else:
                res.append([
                    nums[i],
                    nums[left],
                    nums[right]
                ])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
        
    return res

print(threeSum([-1,0,1,2,-1,-4]))
# print(threeSum([0,1,1]))
# print(threeSum([0,0,0]))
