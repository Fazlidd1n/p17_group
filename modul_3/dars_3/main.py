def division(num):
    def inner(function):
        def wrapper(*args):
            result = function(*args)
            return result / num

        return wrapper

    return inner


@division(3)
def a_(*args):
    return sum(args)


print(a_(1, 2, 3))
