text = input('Введите свой текст; ')

txet = text.replace(' ', '')

upletters = sum(1 for c in txet if c.isupper())

lowletters = sum(1 for c in txet if c.islower())

alltext = sum(1 for c in txet)

upprc = (upletters/alltext)*100

lowprc = (lowletters/alltext)*100

print(f'''Всего букв в тексте: {alltext}\nПроцент букв верхнего регистра: {upprc}%\nПроцент букв нижнего регистра: {lowprc}%''')

