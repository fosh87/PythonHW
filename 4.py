n = int(input("Введите целое положительное число:"))
n_temp = 0
n_result = 0
while n > 0:
    n_temp = n % 10
    if n_result < n_temp:
        n_result = n_temp

    n = n // 10
print(n_result)
