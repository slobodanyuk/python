import random


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


def add_space(x):
    """
    Функция добавляет пустоты между числами в карточках игроков
    """

    for i in range(4):
        i = random.randint(0, 4)
        x.insert(i, '')

    return x


def set_conditions():
    """
    Функция добавляет пустоты между числами в карточках игроков
    """
    raw_list = []
    fin_list = []
    while len(raw_list) != 30:
        x = random.randint(1, 90)
        if not x in raw_list:
            raw_list.append(x)

    while len(raw_list) > 0:
        fin_list = fin_list + add_space(sort_to_max(raw_list[0:5]))
        raw_list[0:5] = []

    return fin_list


def status():
    """
    Функция выводит на экран информацию о новом бочонке, а также карточки игроков
    """

    print('Новый бочонок:', keg, '(Осталось ', len(keg_list), ')')
    print ('-' *10, 'Ваша карточка', '-' *10, '\n',
          ppad1, '\n', ppad2, '\n', ppad3, '\n', '-' *35)
    print('-' * 7, 'Карточка компьютера', '-' * 7, '\n',
         aipad4, '\n', aipad5, '\n', aipad6, '\n', '-' * 35)


def draw_keg():
    """
    Функция забирает случайный бочонок из списка
    """
    draw = random.choice(keg_list)
    keg_list.remove(draw)
    return draw


def get_answer():
    """
    Функция предлагает игроку сделать выбор
    """
    print("Зачеркнуть цифру? (y/n). Выйти в главное меню (q)")
    answer = input()

    return answer


def process_answer():
    """
    Функция обрабатывает ответ игрока
    """

    if answer == "y":
          if keg in play_kegs[0:27]:
                 q = play_kegs.index(keg)
                 play_kegs[q] = '-'
          else:
                 return "lose1"
    elif answer == "n":
          if keg in play_kegs[0:27]:
                 return "lose2"
          else:
                 if keg in play_kegs[27:54]:
                     w = play_kegs.index(keg)
                     play_kegs[w] = '-'


def check_winner():
    """
    Функция проверяет есть ли победитель в игре после действия игрока
    """
    win = ""
    try:
        win = "".join(play_kegs[0:27])
        return "you_win"
    except Exception:
        pass

    try:
        win = "".join(play_kegs[27:54])
        return "ai_win"
    except Exception:
        pass

def game_rules():
    print(" "*30,"== Лото ==" ,"\n",
          " "*25,"Правила игры в лото","\n",
        "Игра ведется с помощью специальных карточек, на которых отмечены числа,","\n",
        "и фишек (бочонков) с цифрами.","\n",
        "Количество бочонков — 90 штук (с цифрами от 1 до 90).", "\n",
        "Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,","\n",
        "расположенных по возрастанию. Все цифры в карточке уникальны.","\n",
        "В игре 2 игрока: пользователь и компьютер.","\n",
          "Каждому в начале игры выдается случайная карточка","\n",
          "Каждый ход выбирается один случайный бочонок и выводится на экран.","\n",
          "Также выводится карточка игрока и карточка компьютера.","\n",
          "Пользователю предлагается зачеркнуть цифру на карточке или продолжить","\n",
          "Если игрок выбрал 'зачеркнуть':","\n",
          "    Если цифра есть на карточке - она зачеркивается и игра продолжается.","\n",
          "    Если цифры на карточке нет - игрок проигрывает и игра завершается.","\n",
          "Если игрок выбрал 'продолжить':","\n",
          "    Если цифра есть на карточке - игрок проигрывает и игра завершается.","\n",
          "    Если цифры на карточке нет - игра продолжается.","\n","\n"
          " Побеждает тот, кто первый закроет все числа на своей карточке")



while True:
    quitgame = 0
    print("Loto ver 1.0", '\n',
          "1 - Новая игра",'\n'
          " 2 - Правила игры", '\n'
          " 3 - Выйти из игры")
    quitgame = input()
    if quitgame == '1':
        pass
    elif quitgame == '2':
        print(game_rules(), "\n")
        input("Нажмите Enter для запуска игры")
        pass
    elif quitgame == '3':
        break

    keg_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
                71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                81, 82, 83, 84, 85, 86, 87, 88, 89, 90]

    play_kegs = set_conditions()

    while len(keg_list) > 1:

        ppad1 = play_kegs[0:9]
        ppad2 = play_kegs[9:18]
        ppad3 = play_kegs[18:27]

        aipad4 = play_kegs[27:36]
        aipad5 = play_kegs[36:45]
        aipad6 = play_kegs[45:54]

        keg = draw_keg()
        status()
        answer = get_answer()
        if answer == "q":
            break

        if process_answer() == "lose1":
            print("Вы проиграли! В вашей карточке не было числа", keg)
            break
        elif process_answer() == "lose2":
            print("Вы проиграли! В вашей карточке было число", keg)
            break

        if check_winner() == "you_win":
            print("Поздравляю! Вы выиграли!")
            break
        elif check_winner() == "ai_win":
            print("Выиграл компьютер первым собрав все бочонки!")
            break

    print('\n'*2, " " *15, "Game Over", '\n',
          "Нажмите Enter, чтобы выйти в главное меню")
    input()
