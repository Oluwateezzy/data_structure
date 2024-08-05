"""
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.
"""

# # greedy solution
# class Solution:
#     def maxUniqueSplit(self, s: str) -> int:
#         #ababccc
#         temp = ''
#         arr = []

#         for letter in s:
#             temp += letter
#             if temp not in arr:
#                 arr.append(temp)
#                 temp = ''

#         return len(arr)

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backTrack(start, set_str):
            print(set_str, start)
            if start == len(s):
                return len(set_str)
            
            max_str = 0
            for end in range(start + 1, len(s) + 1):
                string = s[start:end]
                print("string: ", string)
                if string not in set_str:
                    set_str.add(string)
                    print("Set string: ", set_str)
                    max_str = max(max_str, backTrack(end, set_str))
                    print(max_str, "max")
                    set_str.remove(string)
            
            return max_str
        
        return backTrack(0, set())
    
sol = Solution()
print(sol.maxUniqueSplit("ababccc"))