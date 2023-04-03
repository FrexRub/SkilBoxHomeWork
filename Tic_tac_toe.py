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
        self.cells = [Cell(True, index) for index in range(1, 10)]


class Player:
    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит

    def __init__(self, name):
        self.name = name
        self.list_cell = []

    def go_new_cell(self, curent_player, to_go):

    def player_to_go(player_1):
            pass


player_1 = Player('Павел')
player_2 = Player('Сергей')
playing_field = Board()


while True:
    random_cell = random.randint(1, 9)
    player_to_go(player_1)