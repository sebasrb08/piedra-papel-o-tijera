
import random
veces = int(input("Digite cuantas veces quiere jugar  "))
juego = ['piedra','papel','tijera']
cont=0
cont2=0
for i in range (veces):
    num = random.randint(0,2)
    usu = input("digite piedra papel o tijera  ")
    if usu == 'piedra' and juego[num] == 'tijera':
        print('gano el usuario')
        cont+=1 
    elif usu == 'piedra' and juego[num] == 'papel':
        print('gano el contrincante')
        cont2+=1
    elif usu == 'papel' and juego[num] == 'tijera':
        print('gano el contrincante')
        cont2+=1
    elif usu == 'papel' and juego[num] == 'piedra':
        print('gano el usuario')
        cont+=1
    elif usu == 'tijera' and juego[num] == 'piedra':
        print('gano el contrincante')
        cont2+=1
    elif usu == 'tijera' and juego[num] == 'papel':
        print('gano el usuario')
        cont+=1
    else:
        print('empate')
print(f'el usuario tiene {cont} puntos ')
print(f'el contrincante tiene {cont2} puntos ')