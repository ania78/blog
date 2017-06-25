def hej(imie):
    if imie == 'Ola':
        print('Hej Ola!')
    elif imie == 'Sonja':
        print('Hej Sonja!')
    else:
        print('Hej nieznajoma!')

hej('imie')

def hej(imie):
	print('Hej ' + imie + '!')


hej("Rachel")

def hej(imie):
    print('Hej ' + imie + '!')

dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']
for imie in dziewczyny:
    hej(imie)
    print('Kolejna dziewczyna')
