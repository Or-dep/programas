n = int(input('digite o ano para verificação:'))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('{} É ano bissexto'.format(n))
else:
    print('{} Esse ano, Não é bissexto'.format(n))
