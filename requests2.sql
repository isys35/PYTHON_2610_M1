SELECT DISTINCT product.model, pc.price
FROM Product JOIN pc ON product.model = pc.model WHERE maker = 'B'
UNION
SELECT DISTINCT product.model, laptop.price
FROM Product JOIN laptop ON product.model = laptop.model WHERE maker = 'B'
UNION
SELECT DISTINCT product.model, printer.price
FROM Product JOIN printer ON product.model = printer.model WHERE maker = 'B'

SELECT maker
FROM Product
WHERE type = 'pc'
EXCEPT
SELECT maker
FROM Product
WHERE type = 'laptop'

SELECT DISTINCT maker
FROM product JOIN pc ON product.model=pc.model
WHERE pc.speed>=450;

SELECT model, price
FROM printer
WHERE price = (SELECT MAX(price) FROM printer)
