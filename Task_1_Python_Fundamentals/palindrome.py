def is_palindrome(x):
  s = str(x)
return s == s[::-1]

print(is_palindrome("TAT"))
