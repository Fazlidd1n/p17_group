a = 9
b = 0

try:
    assert b != 0, "Assertion failed !"
    print(a // b)
except AssertionError as e:
    print(e)
