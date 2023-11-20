a = "Hello .world"

# count
print(a.count("Hello")) # 1

# title
print(a.title()) # Hello .World

# capitalize
print(a.capitalize()) # Hello .world

# replace
print(a.replace("ll", "")) # Heo .world

a = "bottirjon"
# find
print(a.find("p" , 2)) # -1 , +->

# index
# print(a.index("p")) # error , +->

a = "hello|wor|ld"
# split
print(a.split("|",3))

# rsplit
print(a.rsplit("|", 1))

# join
print(",".join(["Hello", "world" , "1234"]))

a  ="pdp"
# upper
print(a.upper())

a = "pDP"
# casefold
print(a.casefold())

# lower
print(a.lower())

a = "pDp" # PdP

# swapcase
print(a.swapcase())

a = "1wertyui2"
# startswith
print(a.startswith("1we"))
print(a.endswith("ui2"))

year = "2019"
month = "2"

# ljust
print(month.rjust(10, " "))
print(month.ljust(10, " "))

message = "        hello world      ...."
# strip
print(message)
print(message.strip(".").strip())

# lstrip
# rstrip


message = "hello world"
print(message[:-2])

# rfind
print(message.rfind("l", 0 , -2))


a = "123"
# encode
u = a.encode("utf-8")
print(u.decode())



a = "cabc"
# rindex
print(a.rindex("c", -4 ))



a = "abc.cpp"
# removeprefix
print(a.removeprefix("a"))


# removesuffix
print(a.removesuffix(".py"))


a = "한국어"
# isascii
print(a.isascii())

a = "   "
# isspace
print(a.isspace())


a = "\u00B2"
# isdecimal
print(a.isdecimal())


# isdigit
print(a.isdigit())




a = "\u00B2"
# isnumeric
print(a.isnumeric())


a = "dasfdgf"
# isalpha
print(a.isalpha())


a = "123.gh"
# isalnum
print(a.isalnum())

a = "123"
# zfill
print(a.zfill(4))


a = "Hello {1} , age: {0}"
# format
print(a.format("24" , "Botirjon" ))



name = "Botirjon"
age = 24
# f string
print(f"Hello {name} , age: {age}")


# for i in a.__dir__():
#     if not "_" in i:
#         print(i)

m= 4
m = max(max([1, 2, 3]),m)

