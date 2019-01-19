# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    """
    Выявляет числа, у которых сумма первых и последних цифр равны
    (только для шестизначного числа)
    """
    temp_list = []
    i = 0
    while i <= 5:
        temp = int(ticket_number[i])
        temp_list.append(temp)
        i += 1
    if sum(temp_list[:3]) == sum(temp_list[-3:]):
        return "Поздравляю! Номер счастливый "
    else:
        return "Номер не счастливый. Попробуйте снова"


num = input("Введите шестизначное число для проверки:")
print(lucky_ticket(num))

            Normal

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(List):
    """
    Функция сортирует значения в списке по возрастающей
    """
    temp = []
    while len(List) > 0:
        left = List[0]
        for i in List:
            if i <= left:
                left = i
        List.remove(left)
        temp.append(left)
    List = temp
    return List

Lisst = [4, 7, 15, 3, 8, 1, 8, -20]
print(sort_to_max(Lisst))