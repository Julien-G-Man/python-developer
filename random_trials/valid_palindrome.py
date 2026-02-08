def isPalindrome(s: str) -> bool:
   #remove all non alphanumeric hcaracters and convert to lowercase
   #s = ''.join(c for c in s if c.isalnum()).lower()
   for c in s:
      if c.isalnum():
         s = ''.join(c)
   
   # compare the string with its reverse      
   return s == s[::-1]

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))