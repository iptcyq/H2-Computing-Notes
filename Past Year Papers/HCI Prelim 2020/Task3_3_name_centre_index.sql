SELECT Product.ProductCode, Product.Name, Product.Location, Product.Price, Cake.ServingSize 
FROM Product INNER JOIN Cake On Product.ProductCode = Cake.ProductCode 
WHERE Cake.Shape = 'Circle'