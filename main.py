from random import randint
star = input('Приветствую, для активации систему "Бабуля" нажмите "1", в ином случае нажмите любую другую клавишу для завершения программы ')
if star == '1':
    print('ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!')
    n = input()
    d = 0
    while (True):
        if n == "ПОКА!":
            d += 1
        else:
            d = 0
        if d == 3:
            print("ДО СВИДАНИЯ, МИЛЫЙ!")
            break
        if not n.isupper():
            print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
        else:
            year = randint(1930, 1950)
            print(f"НЕТ, НИ РАЗУ С {year} ГОДА!")
        n = input()
else:
    print('Программа завершенна')