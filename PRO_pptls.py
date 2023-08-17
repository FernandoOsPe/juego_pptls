# Piedra, Papel, Tijeras, Lagarto, Spock
import random
print('~tijeras cortan papel')
print('~papel cubre piedra')
print('~piedra aplasta lagarto')
print('~lagarto envenena spock')
print('~spock rompe tijeras')
print('~tijeras decapita lagarto')
print('~lagarto devora papel')
print('~papel desautoriza spock')
print('~spock destruye piedra')
print('~piedra aplasta tijeras')
options = ('piedra', 'papel', 'tijeras', 'lagarto', 'spock')

rounds = 1
computer_wins = 0
user_wins = 0

while True:

    print('*' * 20)
    print('ROUND', rounds)
    print('JUGADOR => ', user_wins)
    print('COMPUTADORA => ', computer_wins)
    print('*' * 20)

    user = input('Piedra, Papel, Tijeras, Lagarto, Spock => ').lower()
    if not user in options:
        print("ESTA OPCION NO ES VALIDA")
        continue
    computer = random.choice(options)

    print('JUGADOR PIDE =>', user)
    print('COMPUTADORA PIDE =>', computer)

    if user == computer:
        print('!Es un empate¡')
    elif user == 'tijeras' and computer == 'papel':
        print('¡GANASTE!')
        user_wins += 1
    elif user == 'papel' and computer == 'piedra':
        print('¡GANASTE!')
        user_wins += 1
    elif user == 'piedra' and computer == 'lagarto':
        print('¡GANASTE!')
        user_wins += 1
    elif user == 'lagarto' and computer == 'spock':
        print('¡GANASTE!')
        user_wins += 1
    elif user == 'spock' and computer == 'tijeras':
        print('¡GANASTE!')
        user_wins += 1
    elif user == 'tijeras' and computer == 'lagarto':
        print('¡GANASTE!')
        user_wins += 1
    elif user == 'lagarto' and computer == 'papel':
        print('¡GANASTE!')
        user_wins += 1
    elif user == 'papel' and computer == 'spock':
        print('¡GANASTE!')
        user_wins += 1
    elif user == 'spock' and computer == 'piedra':
        print('¡GANASTE!')
        user_wins += 1
    elif user == 'piedra' and computer == 'tijeras':
        print('¡GANASTE!')
        user_wins += 1
    else:
        print('!LO SIENTO PERDISTE¡')
        computer_wins += 1

    if user_wins == 3:
        print('ERES EL GANADOR👍, ¡FELICIDADES!')
        break
    if computer_wins == 3:
        print('¡LO SIENTO🙁!, HAS PERDIDO')
        break
    rounds += 1
