"""
    You are given a 0-indexed string word and an integer k.

At every second, you must perform the following operations:

Remove the first k characters of word.
Add any k characters to the end of word.
Note that you do not necessarily need to add the same characters that you removed. However, you must perform both operations at every second.

Return the minimum time greater than zero required for word to revert to its initial state.

 

Example 1:

Input: word = "abacaba", k = 3
Output: 2
Explanation: At the 1st second, we remove characters "aba" from the prefix of word, and add characters "bac" to the end of word. Thus, word becomes equal to "cababac".
At the 2nd second, we remove characters "cab" from the prefix of word, and add "aba" to the end of word. Thus, word becomes equal to "abacaba" and reverts to its initial state.
It can be shown that 2 seconds is the minimum time greater than zero required for word to revert to its initial state.
Example 2:

Input: word = "abacaba", k = 4
Output: 1
Explanation: At the 1st second, we remove characters "abac" from the prefix of word, and add characters "caba" to the end of word. Thus, word becomes equal to "abacaba" and reverts to its initial state.
It can be shown that 1 second is the minimum time greater than zero required for word to revert to its initial state.
Example 3:

Input: word = "abcbabcd", k = 2
Output: 4
Explanation: At every second, we will remove the first 2 characters of word, and add the same characters to the end of word.
After 4 seconds, word becomes equal to "abcbabcd" and reverts to its initial state.
It can be shown that 4 seconds is the minimum time greater than zero required for word to revert to its initial state.
"""

class Solution3:
  def z_function(self, s):
    z, l, r, n = [0] * len(s), 0, 0, len(s)
    for i in range(1, n):
      if i < r:
        z[i] = min(r - i, z[i - l])

      while i + z[i] < n and s[i + z[i]] == s[z[i]]:
        z[i] += 1

      if i + z[i] > r:
        l, r = i, i + z[i]

    return z

  def minimumTimeToInitialState(self, s: str, k: int) -> int:
    z, n, res = self.z_function(s), len(s), 1

    for i in range(k, n, k):
      if z[i] == n - i:
        return res
      res += 1
    print(res)
    return res
  
  

#   class Solution:
#     def minimumTimeToInitialState(self, word: str, k: int) -> int:
#         z = [0] * len(word)
#         res = 1

#         if word == len(word)*word[0]:
#             return res

#         for i in range(1, len(word)):
#             count = 0
#             for j in range(len(word) - i):
#                 if word[i + j] == word[j]:
#                     count += 1
#                 else:
#                     break
#             z[i] = count
            
#         for i in range(k, len(word), k):
#             if z[i] == len(word) - i:
#                 return res
#             res += 1
#         return res
        
# class Solution:
#     def minimumTimeToInitialState(self, word: str, k: int) -> int:
#         if word == len(word)*word[0]:
#             return 1
#         if len(word) % k != 0:
#             return 1
#         return len(word) // k

# class Solution:
#     def minimumTimeToInitialState(self, word: str, k: int) -> int:
#         t = 0
#         while True:
#             scrambled = self.doF(word, k)
#             t = t + 1
#             if scrambled == word:
#                 return t
#             word = scrambled
    
#     def doF(self, word, k):
#         first_k = word[:k]
#         remaining = word[k:]
#         return remaining + first_k
    
#     abacaba
#     caba
#     [0, 0, 1, 0, 3, 0, 1]

#     [0, 0, 1, 0, 3, 0, 1]
#     [0, 0, 1, 0, 3, 0, 1]
#     [0, 0, 1, 0, 3, 0, 1]
#     [0, 0, 0, 0, 3, 0, 0, 0]
#     [0, 0, 0, 0, 3, 0, 0, 0]


# class Solution:
#     def minimumTimeToInitialState(self, word: str, k: int) -> int:
#         n = len(word)
#         res = 1
#         current = word
        
#         # Perform the operations until the string reverts
#         while True:
#             # Remove first k characters and append them to the end
#             current = current[k:] + current[:k]
#             if current == word:
#                 return res
#             res += 1

class Solution2:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        res = 1
        z = [0] * len(word)
        
        for i in range(1, len(word)):
            count = 0
            for j in range(len(word) - i):
                if word[i + j] == word[j]:
                    count += 1
                else:
                    break
            z[i] = count
            
        for i in range(k, len(word), k):
            if z[i] == len(word) - i:
                return res
            res += 1
        return res

s = Solution2()
print(s.minimumTimeToInitialState("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 1))