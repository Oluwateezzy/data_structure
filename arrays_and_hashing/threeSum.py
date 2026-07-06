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