def uppercase(func):

    def wrapper():
        original_result = func()
        uppper_result = original_result.upper()
        return uppper_result
    return wrapper


@uppercase
def greet():
    return "let's decorate"


def main():
    print(greet())


if __name__ == '__main__':
    main()
