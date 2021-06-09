y = 1

while True:
    out2 = f"{y} + "

    if len(out2) % 16 == 0:
        print(out2)
        print(f"y: {y}")
        print(f"bytes: {len(out2)}")
        break

    y *= 10
