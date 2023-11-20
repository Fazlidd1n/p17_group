s = "abcde"
goals = "deabc"

# for i in range(len(s)):
#     if s[i:] + s[:i] == goals:
#         print(True)
#         break
# else:
#     print(False)

print(goals in s*2)