s = input("Enter first string: ")
t = input("Enter second string: ")

if len(s) != len(t):
    print(False)
else:
    seen = {}

    for char in s:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1

    is_anagram = True

    for char in t:
        if char not in seen:
            is_anagram = False
            break

        seen[char] -= 1

        if seen[char] < 0:
            is_anagram = False
            break

    print(is_anagram)