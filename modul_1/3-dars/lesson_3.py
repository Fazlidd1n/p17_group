# n : str = input("soz kiriting : ")
# print(n[:len(n)//2])

#type casting tipdan tipga otqazw
#type hasting

# a: str = input("son kiriting : ")
# s = 0
# for i in a:
#     s+=int(i)
# print(s)

n : str = input("son kiriting :")
start = 0
while start < len(n):
    if n[start]!="5":
        print(n[start],end=" ")
    start+=1
