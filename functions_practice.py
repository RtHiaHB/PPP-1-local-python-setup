def hello():
    print("Hello!")


def pack(a, b, c):
    foo = []
    foo.append(a)
    foo.append(b)
    foo.append(c)
    return foo


def eat_lunch(foo):
    if len(foo) != 0:
        for i in range(0, len(foo)):
            if i == 0:
                print(f'First I eat {foo[i]}')
            else:
                print(f'Next I eat {foo[i]}')
    else:
        print("My lunchbox is empty!")


hello()
lunchbox = pack("apple", "sammich", "water")
print(lunchbox)
eat_lunch(lunchbox)
