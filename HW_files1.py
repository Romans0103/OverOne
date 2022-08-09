input = open('input.txt', 'r')
for num in input:
    n = num.split()
n_1 = int(n[0])
n_2 = int(n[1])
input.close()
output = open('output.txt', 'w')
output.write(str(n_1 - n_2))
output.close()