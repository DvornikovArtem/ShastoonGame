import random
from enum import Enum


class Cermello_Data:
    def __init__(self):
        self.data = None

    def read_Cermello_file(self):
        data = {}
        file_path = r"C:\Users\YourName\Documents\optimal_strategys.txt"
        with open('optimal_strategys', 'r') as file:
            for line in file:

                line = line.split()

                prev_key = line[0][1:len(line[0]) - 1]
                prev_key = prev_key.split(',')

                if prev_key[0] == '':
                    prev_key = (0,)
                else:
                    prev_key = [int(x) for x in prev_key]

                prev_key = tuple(prev_key)

                data[prev_key] = float(line[1])

        return data


# Класс всех возможных стратегий
class Strategy(Enum):
    # Стратегия 1: если у игрока есть возможность походить, то он ходит и делает выбор хода случайным образом
    RANDOM_MOVES = 1

    # Стратегия 2: игрок заранее ничего не продумывает, он каждый выбор на каждом ходу делает из предположения теории вероятности
    # Игрок не переворачивает ту фишку (или те фишки), вероятность выбить которые в будущем больше, чем ту (тех), которые он перевернул
    # Тут нельзя пропустить ход
    FORWARD_PROBABILITIES = 2

    # Стратегия 3: игрок заранее проанализировал всю игру по методу Цермелло и знает, как ходить в каждой из ситуаций так, чтобы
    # выиграть с наибольшей вероятностью
    CERMELLO_METHOD = 3

    # Стратегия 4: если x+y >= 7 - закрываем её, иначе закрываем x, y.
    # Если после хода из фишек 1-6 остаётся только одна фишка 1 или 2, то ход стоит пропустить.
    DVORNIKOV_METHOD = 4


# Класс игрока
class Player:
    def __init__(self, player_coins: list[int], can_player_skip_move: bool = False, player_strategy: Strategy = None):
        self.player_coins = player_coins
        self.can_player_skip_move = can_player_skip_move
        self.player_strategy = player_strategy

        # Выиграл ли игрок?
        self.is_over = False

    # Метод броска двух кубиков
    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)



    # Метод совершения хода
    def make_move(self, x: int, y: int, data: dict):

        possible_moves = [False, False]

        if not self.player_coins[x] and not self.player_coins[y]:
            possible_moves[0] = True

        if not self.player_coins[x + y]:
            possible_moves[1] = True

        # Стратегия 1
        if self.player_strategy == Strategy.RANDOM_MOVES:

            move = -1
            if all(possible_moves):
                move = random.randint(0, 1)

            if possible_moves == [True, False]:
                self.player_coins[x] = 1
                self.player_coins[y] = 1

            elif possible_moves == [False, True]:
                self.player_coins[x + y] = 1

            elif move == 0:
                self.player_coins[x] = 1
                self.player_coins[y] = 1

            else:
                self.player_coins[x + y] = 1

        # Стратегия 2
        if self.player_strategy == Strategy.FORWARD_PROBABILITIES:
            if possible_moves == [True, False]:
                self.player_coins[x] = 1
                self.player_coins[y] = 1

            elif possible_moves == [False, True]:
                self.player_coins[x + y] = 1

            else:
                player_coins1 = self.player_coins.copy()
                player_coins2 = self.player_coins.copy()
                player_coins1[x] = 1
                player_coins1[y] = 1
                player_coins2[x + y] = 1

                # Сравниваем вероятности
                p1 = 0
                if x + y > 6:
                    p1 = (x + y) / 36
                else:
                    p1 = ((x + y) + 2 * (player_coins1[1:7].count(1) - 1)) / 36

                p2x, p2y = 0, 0
                # p2x = (x + 2 * (player_coins1[1:7].count(1) - 1))/36
                # p2y = (y + 2 * (player_coins1[1:7].count(1) - 1)) / 36
                # p2 = p2x + p2y

                p2x = [[a, b] for a in range(1, 7) for b in range(1, 7) if (a == x and player_coins2[b] == 0) or
                       (b == x and player_coins2[a] == 0) or
                       (a + b == x)]
                p2y = [[a, b] for a in range(1, 7) for b in range(1, 7) if (a == y and player_coins2[b] == 0) or
                       (b == y and player_coins2[a] == 0) or
                       (a + b == y)]
                p2 = p2x + p2y
                p2 = set(tuple(sublist) for sublist in p2)
                p2 = len(p2) / 36

                if p1 > p2:
                    self.player_coins[x] = 1
                    self.player_coins[y] = 1
                else:
                    self.player_coins[x + y] = 1

        # Стратегия 3
        if self.player_strategy == Strategy.CERMELLO_METHOD:

            player_coins1 = self.player_coins.copy()
            player_coins2 = self.player_coins.copy()
            player_coins1[x] = 1
            player_coins1[y] = 1
            player_coins2[x + y] = 1

            # Нужно из (0, 0, 1, 1, ...) получить (3, 4, ...)
            player_coins_reformed = ()
            for coinID in range(1, len(self.player_coins)):
                coin = self.player_coins[coinID]
                if coin == 0:
                    player_coins_reformed += (coinID,)

            player_coins1_reformed, player_coins2_reformed = (), ()

            for coinID in range(1, len(player_coins1)):
                coin = player_coins1[coinID]
                if coin == 0:
                    player_coins1_reformed += (coinID,)

            for coinID in range(1, len(player_coins2)):
                coin = player_coins2[coinID]
                if coin == 0:
                    player_coins2_reformed += (coinID,)

            #print(f'coins = {self.player_coins[1:]}')
            #print(f'coins = {player_coins_reformed}')

            #print(f'coins = {player_coins1[1:]}')
            #print(f'coins = {player_coins1_reformed}')

            #print(f'coins = {player_coins2[1:]}')
            #print(f'coins = {player_coins2_reformed}')


            if len(player_coins_reformed) == 0:
                player_coins_reformed = (0,)

            if len(player_coins1_reformed) == 0:
                player_coins1_reformed = (0,)

            if len(player_coins2_reformed) == 0:
                player_coins2_reformed = (0,)

            time_if_flip_x_and_y = data[player_coins1_reformed]
            time_if_flip_x_plus_y = data[player_coins2_reformed]
            time_if_flip_nothing = data[player_coins_reformed]

            time_minimum = min(time_if_flip_x_and_y, time_if_flip_x_plus_y, time_if_flip_nothing)

            if time_minimum == time_if_flip_x_and_y:
                self.player_coins[x] = 1
                self.player_coins[y] = 1

            elif time_minimum == time_if_flip_x_plus_y:
                self.player_coins[x + y] = 1


        # Стратегия 4
        if self.player_strategy == Strategy.DVORNIKOV_METHOD:

            player_coins1 = self.player_coins.copy()
            player_coins2 = self.player_coins.copy()
            player_coins1[x] = 1
            player_coins1[y] = 1
            player_coins2[x + y] = 1

            is_one_alone1, is_one_alone2, is_two_alone1, is_two_alone2 = False, False, False, False
            if player_coins1[1:7].count(0) == 1:
                if player_coins1[1] == 0:
                    is_one_alone1 = True
                if player_coins1[2] == 0:
                    is_two_alone1 = True

            if player_coins2[1:7].count(0) == 1:
                if player_coins2[1] == 0:
                    is_one_alone2 = True
                if player_coins2[2] == 0:
                    is_two_alone2 = True

            #print(player_coins1[1:7])
            #print(player_coins2[1:7])
            #print(possible_moves)

            #input()

            if possible_moves == [True, False] and not is_one_alone1 and not is_two_alone1:
                self.player_coins[x] = 1
                self.player_coins[y] = 1

            elif possible_moves == [False, True] and not is_one_alone2 and not is_two_alone2:
                self.player_coins[x + y] = 1

            elif possible_moves == [True, True]:

                if x + y >= 7:
                    self.player_coins[x + y] = 1
                elif not is_one_alone1 and not is_two_alone1:
                    self.player_coins[x] = 1
                    self.player_coins[y] = 1



        # Проверка, закончил ли игрок данным ходом игру
        if all(self.player_coins[1:13]):
            self.is_over = True

        return self.player_coins


class ShastoonGame:

    # Инициализируем игру с 3 параметрами:
    # - количество игроков;
    # - можно ли игрокам пропускать ход;
    # - какую стратегию использует каждый игрок

    def __init__(self, number_of_players: int = 1, can_players_skip_move: bool = False,
                 players_strategys: list[Strategy] = None):

        if len(players_strategys) != number_of_players:
            raise ValueError(
                f"Количество указанных стратегий ({len(players_strategys)}) не соответствует количеству игроков ({number_of_players}).")

        self.number_of_players = number_of_players
        self.can_players_skip_move = can_players_skip_move
        self.players_strategys = players_strategys

        # Создаём каждому игроку своё игровое поле из 12 фишек (нумерация с 1)
        self.players_coins = [[0] * 13 for i in range(number_of_players)]

        # Победил ли кто-либо из игроков?
        self.is_anyone_over = False

        # Закончен ли круг?
        self.is_circle_complete = False

        # Закончена ли игра?
        self.is_game_over = False

        # За сколько ходов завершена игра?
        self.moves_count = 0

        # Номера игроков-победителей
        self.winners = []

        #print("Игра успешно создана!")

    # Метод начала игры
    def play(self):
        #print("Игра началась!\n")

        data = {}
        for strategy in self.players_strategys:
            if strategy == Strategy.CERMELLO_METHOD:
                cermello_table = Cermello_Data()
                data = cermello_table.read_Cermello_file()

        # Пока какой-либо игрок не победил и пока круг не закончен
        while not self.is_anyone_over or not self.is_circle_complete:

            #print(f"\nХод {self.moves_count + 1}")

            for playerID in range(self.number_of_players):
                player = Player(player_coins=self.players_coins[playerID],
                                can_player_skip_move=self.can_players_skip_move,
                                player_strategy=self.players_strategys[playerID])

                # Кидаем кубик
                x, y = player.roll_dice()

                #print(f"Игроку {playerID + 1} выпало {x} и {y}")
                #print(f"Игровое поле игрока {playerID + 1} до   : {self.players_coins[playerID][1:13]}")

                # Обновляем поле игрока
                self.players_coins[playerID] = player.make_move(x, y, data)

                #print(f"Игровое поле игрока {playerID + 1} после: {self.players_coins[playerID][1:13]}")

                # Проверяем, победил игрок или нет
                if player.is_over:
                    self.is_anyone_over = True
                    self.winners.append(playerID + 1)

                if playerID == self.number_of_players - 1:
                    self.is_circle_complete = True
                    self.moves_count += 1
                else:
                    self.is_circle_complete = False

        #print(f"\nИгра закончена за {self.moves_count} ход(-а)(-ов).\n"
        #      f"Победил(-и) игрок(-и) {self.winners}")
