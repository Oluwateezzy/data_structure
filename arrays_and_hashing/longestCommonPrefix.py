from typing import List

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_val = sorted(strs, key=len)[0]
        print(first_val)
        result = ""

        for i in range(len(first_val)):
            count = 0
            for st in strs:
                print(st[i], first_val[i])
                if st[i] == first_val[i]:
                    pass
                else:
                    return result
            count += 1
            result += first_val[i]
            print(f"result {i} - {result}")
            print(count)
            if len(first_val) == count:
                return result
        return result

sol = Solution()
print(sol.longestCommonPrefix(["ab", "a"]))