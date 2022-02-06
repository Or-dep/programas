from datetime import date
ano = date.today().year
nasc = int(input('digite seu ano de nascimento:'))
id = ano - nasc
if id < 18:
    print('Você não precisa se alistar!')
    if id == 17:
        print('Mas, no proximo ano você precisara se alistar!')
elif id == 18:
    print('você precisa se alistar imediatamente!')
elif id > 18:
    print('     \nVocê ja deveria ter se alistado!\n\nCaso já tenha se alistado ignore essa mensagem.')