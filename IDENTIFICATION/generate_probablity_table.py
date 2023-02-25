f2 = open("cum_prob_table.txt", 'w')
# idsorted.txt has 314686575 lines using wc -l
sum = 314686575
probability = float(1) / sum
with open("idsorted.txt") as f:
    i = 0;
    for line in f:
        i = i + 1
        lineinf2 = str(i * probability) + ',' + line.strip() + '\n'
        f2.write(lineinf2)
f2.close()
