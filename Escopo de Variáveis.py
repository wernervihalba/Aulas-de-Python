"""
Escopo de Variáveis
- Existe dois tipos de escopos de variáveis, sendo eles:

1º - Variável Global;
- As variáveis são reconhecidas, ou seja, seu escopo reconhece todo o programa
2º - Variável local.
- São apenas reconhecidas no bloco em que foram declaradas

- Para declarar uma variável em Python fazemos:
número_de_variável = Valor_da_variável

Python é uma línguagem dinâmica. Isso significa que na declaração da variável não colocamos o tipo de dado que ela é.
Esse tipo é atribuído quando atribuírmos valor a mesma.

"""


numero = 42  # exemplo de variável global
print(numero)
print(type(numero))

número = 'Thawanna'
print(número)
print(type(número))
