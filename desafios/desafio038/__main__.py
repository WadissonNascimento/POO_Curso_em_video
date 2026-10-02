from classes import *

p1 = Produto("mouse", 320)
p2 = Produto("Monitor", 830)

c1 =  Carrinho()
c1 = c1 + p1 + p2
c2 = c1 + p1 + p2

print(c1)
