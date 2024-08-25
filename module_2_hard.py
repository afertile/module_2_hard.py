i = int(input())
result = ''
if not(3 <= i <= 20):
    print("Неправильное число")
    exit()
for j in range(1, 20):
    for k in range(j, 20):
        if i % (j + k) == 0 and j != k:
            result += str(j) + str(k)
print(result)