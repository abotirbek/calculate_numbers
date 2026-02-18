#17 Bo'luvchilar soni
n = int(input("Qaysi sonning bo'luvchilar sonini aniqlamoqchisiz: "))
num = 0
for x in range(1,n+1):
    if n % x == 0:
        num += 1
print(num)
