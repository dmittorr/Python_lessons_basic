# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    input_number = str(number)
    point_number = input_number.find('.')
    first_digit = int(input_number[:point_number])
    round_digit = int(input_number[point_number+1:ndigits+point_number+1])
    next_round_digit = int(input_number[ndigits+point_number+1])
    if next_round_digit >= 5:
        round_digit += 1
        if len(str(round_digit)) > ndigits:
            first_digit += 1
            round_digit = 0
    return float(str(first_digit)+'.'+str(round_digit))
    # pass


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    i = 0
    sum1 = 0
    sum2 = 0
    while i < 3:
        sum1 = ticket_number % 10 + sum1
        ticket_number = ticket_number // 10
        i += 1
    while i < 6:
        sum2 = ticket_number % 10 + sum2
        ticket_number = ticket_number // 10
        i += 1
    if sum1 == sum2:
        return "Повезло, билет счастливый"
    else:
        return "В следующий раз повезёт"

    # pass


print(lucky_ticket(123006))
print(lucky_ticket(123210))
print(lucky_ticket(436751))
