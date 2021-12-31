def welcom(): #правила игры
    print("*******************************************")
    print("         Добро пожаловать в игру")
    print("             крестики-нолики")
    print("*******************************************")
    print("                 Правила:")
    print("      учасникам по-очереди необходимо ")
    print(" вводить координаты от 0 до 2 через пробел.")
    print("     Побеждает игрок, который первым")
    print("          выстроит свою фигуру")
    print("  по вертикали, горизонтали или диагонали.  ")
    print("*******************************************")
    print()

welcom()


field = [[" "] * 3 for i in range(3)]

def show_field(): # вывод игрового поля на экран
    print("  | 0 | 1 | 2 |")
    print("---------------")
    for i in range(3):
        print(i, "|", " | ".join(field[i]), "|")
        print("---------------")


def ask_step(): #запрашиваем координаты
    while True:
        try:
            step = tuple(map(int, input("Ваш ход!\n    Введите координаты ").split()))
            if len(step) != 2:
                print()
                print("Введите два числа!!!")
                print()
                continue

            first_number = step[0]
            second_number = step[1]

            if 0 > first_number or first_number > 2 or 0 > second_number or second_number > 2:
                print()
                print("Координаты вне диапазона")
                print()
                continue

        except ValueError:
            print()
            print("Упс... ")
            print("Введите 2 целых числа!!!")
            print()
            continue

        except KeyboardInterrupt:
            break

        if field[first_number][second_number] != " ":
            print()
            print("Клетка занята")
            print()
            continue
        print()

        return first_number, second_number


def check_win(): #проверка выигрышных комбинаций
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл крестик!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл нолик!!!")
            return True
    return False


def greet(): #запускается игра
    count = 0
    while True:
        count += 1
        show_field()
        if count % 2 == 1:
            print()
            print(" Ходит крестик!")
        else:
            print()
            print(" Ходит нолик!")

        try:
            first_number, second_number = ask_step()
        except TypeError:
            print("Игра была прервана!!!")
            break

        if count % 2 == 1:
            field[first_number][second_number] = "X"
        else:
            field[first_number][second_number] = "0"

        if check_win():
            show_field()
            break

        if count == 9:
            print(" Ничья!")
            break

greet()