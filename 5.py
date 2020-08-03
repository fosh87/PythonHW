proceeds = float(input("Введите сумму выручки вашей фирмы:"))
expense = float(input("Введите сумму издержек вашей фирмы:"))
profit = proceeds - expense
if 0 < profit > expense:
    print(f"У вас прекрасный финансовый результат. Ваша прибыль составила {profit:.2f}, что превышает ваши издержки на сумму {profit - expense:.2f}.")
    rent = profit / proceeds
    personal = int(input("Введите количество сотрудников вашей фирмы:"))
    profit_personal = profit / personal
    print(f"Рентабельность вашей выручки составила {rent:.2f}. Ваша прибыль в расчете на одного сотрудника составляет {profit_personal:.2f}")
else:
    print(
        f"У вас не очень хороший финансовый результат. Ваша прибыль составила {profit:.2f}, что меньше ваших издережк на сумму {expense - profit:.2f}")