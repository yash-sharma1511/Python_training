def is_palindrome(s: str) -> bool:
    rev=s[::-1]
    if s==rev:
        return "True"
    else:
        return "False"
s=input("Enter Word ")
print(is_palindrome(s))    