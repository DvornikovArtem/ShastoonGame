from ShastoonGame import ShastoonGame
from ShastoonGame import Strategy

if __name__ == '__main__':

    results = [0, 0]

    # Определяем стратегии ВСЕХ игроков
    players_strategys = [Strategy.FORWARD_PROBABILITIES, Strategy.CERMELLO_METHOD]

    #players_strategys = [Strategy.DVORNIKOV_METHOD]

    # Создаём игру
    #game = ShastoonGame(number_of_players=1, can_players_skip_move=True, players_strategys=players_strategys)

    # Начинаем игру
    #game.play()

    for i in range(1000):

        # Создаём игру
        game = ShastoonGame(number_of_players=2, can_players_skip_move=True, players_strategys=players_strategys)

        # Начинаем игру
        game.play()

        for winner in game.winners:
            results[winner - 1] += 1

        #results += game.moves_count

    #print(f'Среднее количество ходов для победы: {results/10000}')

    #print(results)
    #print(f"Рандом победил в {round(results[0]/(sum(results)) * 100, 2)}% случаев")
    print(f"Модель 1 победила в {round(results[0] / (sum(results)) * 100, 2)}% случаев")
    print(f"Модель 2 победила в {round(results[1] / (sum(results)) * 100, 2)}% случаев")
    #print(f"Метод Дворникова победил в {round(results[3] / (sum(results)) * 100, 2)}% случаев")

    # coins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # x, y = 6, 2
    # player_coins1 = coins.copy()
    # player_coins2 = coins.copy()
    # player_coins1[x] = 1
    # player_coins1[y] = 1
    # player_coins2[x + y] = 1
    # p1 = 0
    # if x + y > 6:
    #     p1 = (x + y) / 36
    # else:
    #     p1 = ((x + y) + 2 * (player_coins1[1:7].count(1) - 1)) / 36
    #
    # p2 = []
    # p2x, p2y = 0, 0
    # p2x = [[a, b] for a in range(1, 7) for b in range(1, 7) if (a == x and player_coins2[b]==0) or
    #                                                            (b == x and player_coins2[a]==0) or
    #                                                            (a+b==x)]
    # p2y = [[a, b] for a in range(1, 7) for b in range(1, 7) if (a == y and player_coins2[b] == 0) or
    #        (b == y and player_coins2[a] == 0) or
    #        (a + b == y)]
    # # p2x = (x + 2 * (player_coins1[1:7].count(1) - 1)) / 36
    # # p2y = (y + 2 * (player_coins1[1:7].count(1) - 1)) / 36
    # # p2 += [[a, b] for a in range(1, 7) for b in range(1, 7) if ((a == x and player_coins2[a]==0) or
    # #                                                             (a == y and player_coins2[a]==0) or
    # #                                                             (b == x and player_coins2[b]==0) or
    # #                                                             (b == y and player_coins2[b]==0) or
    # #                                                             x == a+b or
    # #                                                             y == a+b)]
    #
    # p2 = p2x + p2y
    # p2 = set(tuple(sublist) for sublist in p2)
    # print(p2x)
    # print(p2y)
    # print(p2)
    # print(p1)
    # print(len(p2)/36)