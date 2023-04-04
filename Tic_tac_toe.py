import random


class Cell:
    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - номер клетки
    def __init__(self, free, num_cell):
        self.free = free
        self.num_cell = num_cell


class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки
    def __init__(self):
        self.cells = [Cell(False, index) for index in range(9)]

    def game_over(self):
        return all([self.cells[index].free for index in range(9)])


class Player:
    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит

    def __init__(self, name, playing_field):
        self.name = name
        self.list_cell = []
        self.playing_field = playing_field

    def info(self):
        print('Ходы игрока {}: {}'.format(self.name, ', '.join([str(i_cell) for i_cell in self.list_cell])))

    def player_to_go(self):
        def checking_cell_groupe(*num_cell):
            fl_cell = []
            for i_cell in num_cell:
                if i_cell in self.list_cell:
                    fl_cell.append(True)
                else:
                    fl_cell.append(False)
            return all(fl_cell)

        def checking_winnings():  # проверка хода если побыдный то True
            if checking_cell_groupe(0, 1, 2):
                result = True
            elif checking_cell_groupe(0, 3, 6):
                result = True
            elif checking_cell_groupe(1, 4, 7):
                result = True
            elif checking_cell_groupe(2, 5, 8):
                result = True
            elif checking_cell_groupe(0, 4, 8):
                result = True
            elif checking_cell_groupe(6, 4, 2):
                result = True
            elif checking_cell_groupe(3, 4, 5):
                result = True
            elif checking_cell_groupe(6, 7, 8):
                result = True
            else:
                result = False
            return result

        while True:
            random_cell = random.randint(0, 8)
            if not self.playing_field.cells[random_cell].free:
                self.list_cell.append(random_cell)
                self.playing_field.cells[random_cell].free = True
                break
        if checking_winnings():
            print('Игрок {} победил'.format(self.name))
            self.info()
            result = True
        elif self.playing_field.game_over():
            print('игра закончена в ничью')
            result = True
        else:
            result = False
        return result


# cоздаем поле и играков
playing_field = Board()
player_1 = Player('Павел', playing_field)
player_2 = Player('Сергей', playing_field)
print('Начало игры')

while True:
    if player_1.player_to_go():
        break
    elif player_2.player_to_go():
        break
    player_1.info()
    player_2.info()
    print()
