n = int(input())
lst, numbers, ord_val, asc, char = [], [], [], [], []
for i in range(n):
    m = input()
    lst.append(m)
if n in range(1, 51):
    for i in lst:
        for j in i:
            a = ord(j)
            asc.append(a)
        for j in reversed(range(len(i) // 2 + 1)):
            j = j - (2 * j)
            numbers.append(j)
        for j in range(1, (len(i) // 2) + 1):
            j = j - (2 * j)
            numbers.append(j)
        for j in range(len(i)):

            value = asc[j] + numbers[j]
            if value < 97:
                value = 123 + (numbers[j])
            ord_val.append(value)
        for j in ord_val:
            c = chr(j)
            char.append(c)
        char.append(" ")
        str1 = ''.join(map(str, char))
        numbers.clear()
        asc.clear()
        ord_val = []
    x = str1.split()
    for i in x:
        print(i)
