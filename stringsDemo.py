# 1. Concatenate two strings
str1 = "Hello"
str2 = "World"
print("Concatenated:", str1 + " " + str2)

# 2. Find length of a string
text = "Python"
print("Length:", len(text))

# 3. Access characters using indexing
print("First character:", text[0])
print("Last character:", text[-1])

# 4. Reverse a string
print("Reversed:", text[::-1])

# 5. Count occurrences of a character
sentence = "programming"
print("Count of 'm':", sentence.count('m'))

# 6. Convert to uppercase and lowercase
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# 7. Check if string is palindrome
word = "madam"
if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

# 8. Remove spaces from a string
spaced = " P y t h o n "
print("Without spaces:", spaced.replace(" ", ""))

# 9. Check if substring exists
if "gram" in sentence:
    print("'gram' found in", sentence)
else:
    print("'gram' not found")

# 10. Replace a word in a string
quote = "I like Java"
quote = quote.replace("Java", "Python")
print("Updated Quote:", quote)

# 11. Split a sentence into words
words = "Python is fun".split()
print("Split words:", words)

# 12. Join list of strings into one string
joined = "-".join(words)
print("Joined with dash:", joined)

# 13. Capitalize first letter of each word
title_text = "welcome to python programming"
print("Title Case:", title_text.title())

# 14. Count vowels in a string
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)
print("Vowel count in", text, ":", vowel_count)

# 15. Remove punctuation from a string
import string
sample = "Hello, World!"
cleaned = "".join(ch for ch in sample if ch not in string.punctuation)
print("Without punctuation:", cleaned)

# 16. Check if a string is alphanumeric
check_str = "Python123"
print("Is Alphanumeric?", check_str.isalnum())

# 17. Find index of first occurrence
print("Index of 'o' in", text, ":", text.find('o'))

# 18. Convert first letter to uppercase (sentence case)
sentence_case = text.capitalize()
print("Sentence case:", sentence_case)
