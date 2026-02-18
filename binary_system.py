#13 ikkilik sanoq sistemasi
n = int(input("10lik sanoq sistemasidagi sonni kiriting: "))
binary = []
while n > 1:
    remainder = n % 2
    binary.append(str(remainder))
    n = n // 2
binary.append(n)
result = ''
while binary:
    num = binary.pop()
    result += str(num)
print(f"Ikkilik sanoq sistemasidagi ko'rinishi: {result}")


#14 o'nlik sanoq sistemasi
n = int(input("2lik sanoq sistemasidagi sonni kiriting: "))
up_down = str(n)[::-1]
num = -1
total = 0
for u in up_down:
    num += 1
    total += int(u) * (2**num)
print(f"10lik sanoq sistemasidagi ko'rinishi: {total}")
