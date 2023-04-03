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

    def info(self):
        for i_cell in self.cells:
            print('номер яейки :', i_cell.num_cell, 'состояние ячейки', i_cell.free)

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

    def player_to_go(self):
        while True:
            random_cell = random.randint(0, 8)
            print(random_cell, self.playing_field.cells[random_cell].free)
            if not self.playing_field.cells[random_cell].free:
                self.list_cell.append(random_cell)
                self.playing_field.cells[random_cell].free = True
                break
        if checking_winnings():
            print('Игрок {} победил'.format(self.name))
            result = True
        elif self.playing_field.game_over():
            print('игра закончена в ничью')
            result = True
        else:
            result = False
        return result

    def checking_winnings(self): #проверка хода если побыдный то True
        print('Ход игрока {}'.format(self.name))
        return True


playing_field = Board()
player_1 = Player('Павел', playing_field)
player_2 = Player('Сергей', playing_field)
print('Начало игры')
playing_field.info()

while True:
    if player_1.player_to_go():
        break
    elif player_2.player_to_go():
        break

playing_field.info()

