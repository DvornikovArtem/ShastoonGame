# Реализация игры, описанной в [файле](README.md)
Весь описываемый далее код приложен на языке программирования `Python`.

Весь код состоит из двух основных частей:
1) класса `ShastoonGame.py`, в котором для простоты реализованы сразу все нужные для игры классы;
2) файла `main.py`, из которого можно запустить игру с любыми нужными Вам условиями.

Далее пойдём по порядку каждого из файлов и посмотрим, как что реализовано.

## Реализация стратегии №1 (полный рандом)
1) Проверяем, какие из ходов x, y и x + y возможны;
2) Если возможен только один их ходов, то ходим им;
3) Если возможны оба хода, то выбираем рандомный ход.

## Реализация стратегии №2 (модель учёта будущей вероятности)
1) Проверяем, какие из ходов x, y и x + y возможны;
2) Если возможен только один их ходов, то ходим им;
3) Если возможны оба хода, то выбираем ход по следующей формуле:

$$ K(p_1, p_2) = p_1 \cdot p(x + y) + p_2 \cdot (p(x) + p(y)), где $$

- K - это функция выигрыша (мы хотим её минимизировать, т.к. чем меньше значение функции, тем больше вероятность выиграть);
- (p<sub>1</sub>, p<sub>2</sub>) - смешанная стратегия игрока (просто вероястности выбрать первый или второй вариант хода);
- p(x + y) - вероятность выбить число x + y на текущем поле, где перевёрнуты фишки x, y;
- p(x) +  p(y) - вероятность выбить число x или y на текущем поле, где перевёрнута фишка x + y.

> **Замечание. Во всех случаях смешанная стратегия превращается в чистую, то есть либо p<sub>1</sub> = 1 и p<sub>2</sub> = 0, либо p<sub>1</sub> = 0 и p<sub>2</sub> = 1.**

## Реализация стратегии №3 (модифицированная модель Цермелло)
1) Проверяем, какие из ходов x, y и x + y возможны;
2) Для каждого из возможных ходов достаём из пространства состояний среднее количество ходов до конца игры;
3) В каком из случае количество ходов минимально, тот ход мы и делаем.

Здесь важно пояснить, откуда мы берём словарь со всеми количествами ходов для каждого из состояний.

Давайте вспомнил простую формулу средней скорости в пути S за время t:

$$ v_{\text{ср}} = \frac{\text{Общее расстояние}}{\text{Общее время}} = \frac{\sum_{i=1}^n \Delta S_i}{\sum_{i=1}^n \Delta t_i} $$

Здесь формула для расчёта среднего количества ходов из состояния S до конца игры вводится аналогично:

$$ t[S] = 1 + \sum \frac{1}{36} \cdot t[S] + \sum \frac{1}{36} \cdot t[S \backslash (x, y)] + \sum \frac{1}{36} \cdot t[S \backslash (x + y)] + \sum min(t[S \backslash (x + y)], t[S \backslash (x, y)]) $$

1) Здесь первое слагаемое - это время, затрачиваемое на текущий ход;
2) Второе слагаемое - это среднее время, затрачиваемое на ожидание хода (то есть пока выпадают те числа, которые не дают ни один доступный вариант хода);
3) Третье слагаемое - это среднее время, которое получается при ходе x, y, когда доступен ТОЛЬКО ход x, y;
4) Четвёртое слагаемое - это среднее время, которое получается при ходе x, y, когда доступен ТОЛЬКО ход x + y;
5) Пятое слагаемое - это среднее МИНИМАЛЬНОЕ время, которое получается при ходе x, y, когда доступны оба хода x, y и x + y.
