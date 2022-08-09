def count_func(f):
    count = 0

    def wrapper():
        nonlocal count
        f()
        count += 1
        print(f'{count}')

    return wrapper


@count_func
def hello():
    print("OverOne!")


hello()
hello()
hello()
