x = 1

while True:
    numbers = {}

    re = x
    im = x
    name = f"{re} + {im}i"

    numbers[name] = [re, im]
    out1 = str(numbers)[:-1] + ", '"

    if len(out1) % 16 == 0:
        print(out1)
        print(f"x: {x}")
        print(f"bytes: {len(out1)}")
        break

    x *= 10
