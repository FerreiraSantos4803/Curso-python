# exercitando os estudos do dia -> manipulação de strings

nome = "eu preciso de um trabalho na área"

print(nome.upper())  # todos maiúsculas
print(nome.title())  # só a primeira inicial
print(nome[::-1])  # noem de trás para frente
print(nome.center(14, "#"))
if nome.startswith("u"):
    print(f'O nome começa com a letra {nome[0]}')
else:
    print(f'O nome começa com a letra {nome[0]}')
