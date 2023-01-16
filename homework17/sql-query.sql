/* Задание 1: Найдите номер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 дол.
Вывести: model, speed и hd.*/
SELECT model, speed, hd FROM pc
WHERE price < 500;

/* Задание 2: Найдите производителей принтеров. Вывести: maker.*/
SELECT DISTINCT maker  FROM Product
WHERE type = 'Printer';

/* Задание 3: Найдите номер модели, объем памяти и размеры экранов ПК-блокнотов, цена которых превышает 1000 дол.*/
SELECT model, ram, screen FROM Laptop
WHERE price>1000;

/* Задание 4: Найдите все записи таблицы Printer для цветных принтеров.*/
SELECT * FROM Printer
WHERE color='y';

/* Задание 5: Найдите номер модели, скорость и размер жесткого диска ПК, имеющих 12x или 24x CD и цену менее 600 дол.*/
SELECT model, speed, hd FROM PC
WHERE price<600 AND (cd = '12x' OR cd = '24x');

/* Задание 6: Для каждого производителя, выпускающего ПК-блокноты c объёмом жесткого диска не менее 10 Гбайт, найти скорости таких ПК-блокнотов. Вывод: производитель, скорость.*/
SELECT DISTINCT Product.maker, Laptop.speed FROM Product
INNER JOIN Laptop ON Product.model = Laptop.model
WHERE Laptop.hd>=10

/* Задание 7: Найдите номера моделей и цены всех имеющихся в продаже продуктов (любого типа) производителя B (латинская буква).*/
SELECT DISTINCT Product.model, PC.price
FROM Product INNER JOIN
     PC ON PC.model = Product.model
WHERE Product.maker = 'B'
UNION
SELECT DISTINCT Product.model, Laptop.price
FROM Product INNER JOIN
    Laptop ON Laptop.model = Product.model
WHERE Product.maker = 'B'
UNION
SELECT DISTINCT Product.model, Printer.price
FROM Product INNER JOIN
    Printer ON Printer.model = Product.model
WHERE Product.maker = 'B'

/* Задание 8: Найдите производителя, выпускающего ПК, но не ПК-блокноты.*/
SELECT maker FROM Product
WHERE type = 'PC'
EXCEPT
SELECT maker FROM Product
WHERE type = 'Laptop'

/* Задание 9: Найдите производителей ПК с процессором не менее 450 Мгц. Вывести: Maker.*/
SELECT DISTINCT maker FROM Product
INNER JOIN PC ON Product.model = PC.model
WHERE PC.speed >=450

/* Задание 10: Найдите модели принтеров, имеющих самую высокую цену. Вывести: model, price.*/
SELECT model, price FROM Printer
WHERE price = (SELECT MAX(price) FROM Printer)