SELECT DISTINCT model, speed, hd
FROM PC
WHERE price < 500
ORDER BY 3 DESC


SELECT DISTINCT maker FROM Product
WHERE type='Printer'
ORDER BY maker ASC


SELECT DISTINCT model, ram, screen FROM Laptop
WHERE price > 1000
ORDER BY model ASC


SELECT DISTINCT code, model, color, type, price FROM Printer
WHERE color = 'y'
ORDER BY code ASC


SELECT DISTINCT model, speed, hd FROM PC
WHERE PC.cd IN ('12X', '24X') AND
price <600


SELECT DISTINCT Product.maker, Laptop.speed
FROM Product, Laptop
WHERE Laptop.model = Product.model AND Laptop.hd >= 10 AND Product.TYPE = 'laptop'


SELECT DISTINCT Product.model, PC.price
FROM Product JOIN PC ON PC.model = product.model WHERE maker = 'B'
UNION
SELECT DISTINCT Product.model, Laptop.price
FROM Product JOIN Laptop ON Laptop.model = product.model WHERE maker = 'B'
UNION
SELECT DISTINCT Product.model, Printer.price
FROM Product JOIN Printer ON Printer.model = product.model WHERE maker = 'B'


SELECT maker FROM Product
WHERE type = 'PC'
EXCEPT
SELECT maker FROM Product
WHERE type = 'Laptop'


SELECT DISTINCT maker FROM Product
JOIN PC ON Product.model = PC.model
WHERE PC.speed >= 450


SELECT model, price
FROM printer
WHERE price = (SELECT MAX(price) FROM printer)

