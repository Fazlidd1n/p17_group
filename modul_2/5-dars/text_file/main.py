with open("test.txt", "a") as file:
    a = int(input("son : "))
    [file.write(f"{i}\n") for i in range(2,a+1,2)]
