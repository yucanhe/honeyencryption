
# locationfield.txt has 3519 lines. so idsorted has 3519*365 * 49 =314686575 ids
f = open("locationfield.txt", 'r')
prefixes = f.readlines()

f2 = open("number.txt", 'w')

for prefix in prefixes:
    for num in range(1, 10000):
        no = prefix.strip() + str(num).zfill(4)
        f2.write(no + "\n")
    f2.flush()

f.close()
f2.close()
