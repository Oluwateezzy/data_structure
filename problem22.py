"""
You are given a character array keys containing unique characters and a string array values containing strings of length 2. You are also given another string array dictionary that contains all permitted original strings after decryption. You should implement a data structure that can encrypt or decrypt a 0-indexed string.

A string is encrypted with the following process:

For each character c in the string, we find the index i satisfying keys[i] == c in keys.
Replace c with values[i] in the string.
Note that in case a character of the string is not present in keys, the encryption process cannot be carried out, and an empty string "" is returned.

A string is decrypted with the following process:

For each substring s of length 2 occurring at an even index in the string, we find an i such that values[i] == s. If there are multiple valid i, we choose any one of them. This means a string could have multiple possible strings it can decrypt to.
Replace s with keys[i] in the string.
Implement the Encrypter class:

Encrypter(char[] keys, String[] values, String[] dictionary) Initializes the Encrypter class with keys, values, and dictionary.
String encrypt(String word1) Encrypts word1 with the encryption process described above and returns the encrypted string.
int decrypt(String word2) Returns the number of possible strings word2 could decrypt to that also appear in dictionary.
"""

from typing import List


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.dictionary = dictionary
        self.key_to_value = {keys[i]: values[i] for i in range(len(keys))}
        
    def encrypt(self, word1: str) -> str:
        enc = ""
        for char in word1:
            if char in self.key_to_value:
                enc += self.key_to_value[char]
            else:
                return ""
        return enc

    def decrypt(self, word2: str) -> int:
        ans = 0 
        for w in self.dictionary:
            if self.encrypt(w) == word2:
                ans += 1
        return ans