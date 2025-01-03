# Игра "Антона Шастуна" или "Балийская игра"
## Общие правила
В Балийскую игру могут играть **любое количество человек** (если играет один человек, то он как бы играет сам с собой).
У каждого игрока есть своё поле (у всех игроков поля одинаковые), которое состоит из 12 фишек с числами от 1 до 12.

![Игровое поле](https://github.com/user-attachments/assets/549e2285-0557-4476-bf79-d42515b7d03f)



## Цель игрока
Как можно быстрее перевернуть все фишки.

## Важное замечание
Если какая-либо фишка уже была перевёрнута, то **обратно перевернуть её уже нельзя**.

## Ход игрока
Ход игрока состоит из броска двух обычных игральных кубиков со значениями от 1 до 6.

После выпадения значений x, y на кубиках игрок на своём игровом поле может либо перевернуть две фишки со значениями x и y, либо же фишку с их суммой x + y.

Но! Если после выпадения чисел x, y на игровом поле игрока уже была перевёрнута фишка x или y, то фишки x, y игрок перевернуть на данном ходу не может (потому что если фишка уже была перевёрнута, то обратно её перевернуть уже нельзя).

Аналогично, если уже была перевернута сумма x + y, то игрок не может перевернуть фишку x + y.

**Важно!** Одним из вариантов хода является его пропуск (даже если у игрока возможность перевернуть фишки).

---

Подытожим. Варианты хода (в каком-то смысле, смешанная стратегия) игрока, если на кубиках выпали числа x, y:

1) **Перевернуть фишки x, y** (эта чистая стратегия возможна, только если на поле до этого хода не были перевёрнуты ни фишка x, ни фишка y);
2) **Перевернуть фишку x + y** (эта чистая стратегия возможна, только если на поле до этого хода не была перевёрнута фишка x + y);
3) **Вообще ничего не переворачивать** (пропуск хода: либо потому что на кубиках выпали неподходящие под первые 2 пункта числа, либо потому что игрок сам не хочет ничего переворачивать).

# Главный вопрос
Как победить в этой игре за как можно более меньшее количество ходов?
