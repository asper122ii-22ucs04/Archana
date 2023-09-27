def linearSearchProduct(ProductList,targetProduct):
  indices=[]
  for index, Product in enumerate(ProductList):
    if Product==targetProduct:
      indices.append(index)
  return indices
Products=["shoes","boot","loafer","shoes","sandal","shoes"]
target="shoes"
result=linearSearchProduct(Products,target)
print(result)