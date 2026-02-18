#18 EKUB
print('Mana shu ko\'rinishda kiriting: EKUK(48,24, ...) yoki EKUB(48,24, ...)')
two_nums = input("Sonlarni kiriting (0): ")

f = two_nums.strip()
fours = f[0:4]
characters = f[4:]
filtered = characters.strip()
filt2 = filtered[1:-1]
items = filt2.split(',')
nums = []
for i in items:
    n = int(i)
    nums.append(n)
# answers = []
if fours.lower() == 'ekub':
    for x in range(min(nums), 0, -1):
        num = 0
        for n in nums:
            if n % x == 0:
                num += 1
        if num == len(nums):
            print(x)
            break

start = 1
for n in nums:
    start *= n
if fours.lower() == 'ekuk':
    for x in range(max(nums), start):
        num = 0
        for n in nums:
            if x % n == 0:
                num += 1
        if num == len(nums):
            print(x)
            break
