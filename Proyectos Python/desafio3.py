import random
usuario=input('Ingresar el nombre de usuario: ')
numeroaleatorio=(print(random.randint(1,100)))
for i in range(8):
    numero = int(input('ingresar un numero para adivinar'))
    if numero == numeroaleatorio:
        print('encontrado')
    else:
        print ('no encontrado')

