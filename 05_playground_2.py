# Encuentra el mayor palíndromo
# https://platzi.com/clases/7967-python-21-dias/63511-encuentra-el-mayor-palindromo/

def find_largest_palindrome(words):
    palindromos = [word for word in words if word.lower()[::-1] == word.lower()]
    return max(palindromos, key=len, default=None)



lst1 = ["racecar", "level", "world", "hello"]
lst2 = ["Platzi", "Python", "django", "flask"]

print(find_largest_palindrome(lst1))
print(find_largest_palindrome(lst2))
