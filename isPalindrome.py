s = "am anapl anacan alpa nam a"

def is_palindrome_recursiva(s):
    s = s.replace(" ","")
    if len(s) <= 1:
        return True
    if s[0] == s[len(s) - 1]:
        return is_palindrome_recursiva(s[1:-1])
    else:
        return False

print(is_palindrome_recursiva(s))
    
