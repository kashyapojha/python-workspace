'''
Maximum Number of Vowels in a substring of given length 
'''
'''
Given a string s and an integer k, return the maximum number of 
vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 1
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 3
Explanation: "lee", "eet" and "ode" contain 2 vowels.
'''

string = str(input("Enter the string:-"))
k = int(input("Enter the value of integer k:-"))
vowels = ["a","e","i","o","u","A","E","I","O","U"]
length = len(string)

max_count = 0
for i in range(length):
    subarray = string[i:i+k]

    count = 0
    for ch in subarray:
        if ch in vowels:
            count +=1
            if count > max_count:
                max_count = count
print("Maximum vowels  = ",max_count)

'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = "aeiou"

        count = 0

        
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        
        for i in range(k, len(s)):

            if s[i-k] in vowels:
                count -= 1

          
            if s[i] in vowels:
                count += 1

            max_count = max(max_count, count)

        return max_count
        '''



