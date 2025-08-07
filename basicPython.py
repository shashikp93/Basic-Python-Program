# Basic Python Programs for Practice

# 1. Hello World
print("1. Hello World")
print("Hello, World!\n")

# 2. Add Two Numbers
print("2. Add Two Numbers")
a = 10
b = 5
print("Sum:", a + b, "\n")

# 3. Check Even or Odd
print("3. Check Even or Odd")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even\n")
else:
    print("Odd\n")

# 4. Find Largest of Three Numbers
print("4. Largest of Three Numbers")
a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))
if a >= b and a >= c:
    print("Largest is:", a, "\n")
elif b >= a and b >= c:
    print("Largest is:", b, "\n")
else:
    print("Largest is:", c, "\n")

# 5. Check Prime Number
print("5. Prime Number Check")
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime\n")
            break
    else:
        print("Prime\n")
else:
    print("Not Prime\n")

# 6. Multiplication Table
print("6. Multiplication Table")
n = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
print()

# 7. Star Pattern
print("7. Star Pattern")
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
print()

# 8. Reverse a String
print("8. Reverse a String")
s = input("Enter a string: ")
print("Reversed:", s[::-1], "\n")

# 9. Palindrome Check
print("9. Palindrome Check")
s = input("Enter string: ")
if s == s[::-1]:
    print("Palindrome\n")
else:
    print("Not Palindrome\n")

# 10. Count Vowels
print("10. Count Vowels in a String")
s = input("Enter string: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in s if ch in vowels)
print("Vowel count:", count, "\n")

# 11. Sum of Elements in List
print("11. Sum of List Elements")
lst = [10, 20, 30, 40]
print("List:", lst)
print("Sum:", sum(lst), "\n")

# 12. Fibonacci Series
print("12. Fibonacci Series")
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
print("\n")

# 13. Factorial Using Loop
print("13. Factorial Calculation")
num = int(input("Enter number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact, "\n")

# 14. Armstrong Number Check (3-digit)
print("14. Armstrong Number Check")
num = int(input("Enter a 3-digit number: "))
sum_of_cubes = sum(int(d)**3 for d in str(num))
if sum_of_cubes == num:
    print("Armstrong number\n")
else:
    print("Not an Armstrong number\n")

# 15. Prime Using Function
print("15. Prime Check using Function")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number: "))
if is_prime(n):
    print("Prime\n")
else:
    print("Not Prime\n")
