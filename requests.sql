SELECT model, speed, hd
FROM pc
WHERE price < 500

SELECT maker
FROM Product
WHERE type = 'Printer'
GROUP BY maker

SELECT model,  ram, screen
FROM laptop
WHERE price > 1000

SELECT code, model, color,  type, price
FROM printer
WHERE color = 'y'

SELECT model, speed, hd
FROM PC
WHERE cd IN ('12x', '24x') AND
price < 600

SELECT DISTINCT Product.maker, Laptop.speed
FROM Product, Laptop
WHERE Laptop.model = Product.model AND Laptop.hd >= 10 AND Product.TYPE = 'laptop'




