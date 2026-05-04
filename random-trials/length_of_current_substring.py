def lengthOfLongestSubstring(s: str) -> int:
   # innitialize the set to store unique characters in the current substrings
   char_set = set()
   
   # initialize two pointers for the sliding window
   left = 0 # left pointer
   max_length = 0 # max length of substring witout repeating characters
   
   # interate over the string
   for right in range(len(s)):
      # while the current character is in the set, remove the leftmost hcaracter
      while  s[right] in char_set:
         char_set.remove(s[left])
         left += 1
         
      # Add the current character to the set
      char_set.add(s[right])   
      
      # update the max length
      max_length = max(max_length, right - left + 1)
   
   return max_length

s = "ifniareinireniboanb"   
print(lengthOfLongestSubstring(s))
