"""
- Recebendo dados do usuário


# Entrada de dados
print('Qual o seu nome?')
nome = input() # input significa entrada de dado.

# Exemplo de print antigo - versão 2.0 do Python
print('Seja Bem-vindo(a) %s' %nome)

print('Qual a sua idade?')
idade = input()

#Processamento

#Saída de dados

#Saída de dados antigo - Python 2.0

print(' %s tem %s anos' % (nome,idade))



"""

#Exemplo de print moderno - apartir do 3.0
# print('Seja bem vindo(a) {0} .format (nome))

#Exemplo de Python mais moderno - Depois da versão 3.7

print('Qual o seu nome?')
nome = input()

print('Qual a sua idade?')
idade = input()

print(f' {nome} tem {idade} anos')

print(f' E nasceu em {2020 - int(idade)}')
