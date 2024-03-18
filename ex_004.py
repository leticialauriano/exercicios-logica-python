digitar = input('Digite algo: ')
tipo_primitivo = type(digitar)
espacos = digitar.isspace()
numero = digitar.isnumeric()
alfabetico = digitar.isalpha()
alfanumerico = digitar.isalnum()
maiuscula = digitar.isupper()
minuscula = digitar.islower()
capitalizada = digitar.istitle()

print(f'Otipo primitivo deste valor é {tipo_primitivo}')
print(f'Só tem espaços? {espacos}')
print(f'É um número? {numero}')
print(f'É um alfabético? {alfabetico}')
print(f'É alfanumérico? {alfanumerico}')
print(f'Está em maiúsculas? {maiuscula}')
print(f'Está em minúsculas {minuscula}')
print(f'Está capitalziada? {capitalizada}')


# digitar = objeto (todo objeto tem características e realiza funcionalidades, tem atributos e métodos.) Com parenteses são métodos.