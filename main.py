def func(num):
    arr1 = []
    num1, num2, num3 = 0, 0, 0
    if not num % 50:
        num1 = num // 50
        if num // 100:
            num2 = num // 100
            if num // 200:
                num3 = num // 200

        for i in range(num3 + 1):
            for j in range(num2 + 1):
                for k in range(num1 + 1):
                    if num == i * 200 + j * 100 + k * 50:
                        ar = (i, j, k)
                        arr1.append(ar)
    return arr1


if __name__ == '__main__':
    print(func(200))