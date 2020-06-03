import random
user = None

CPU = random.choice(['sasso','carta','forbici'])

while user == None:
    user = input('Scegli tra sasso, carta, forbici : ')
    if user not in ['sasso','carta','forbici']:
        print('Devi scegliere tra sasso, carta, forbici !')
        user = None


if user == CPU:
    print('Pareggio')
    print ('\n')
if user == 'sasso':
    if CPU == 'carta':
        print('Hai perso')
        print ('\n')
    elif CPU == 'forbici':
        print('Hai vinto')
        print ('\n')
if user == 'carta':
    if CPU == 'scissor':
        print('Hai perso')
        print ('\n')
    elif CPU == 'sasso':
        print('Hai vinto')
        print ('\n')
if user == 'forbici':
    if CPU == 'roccia':
        print('Hai perso')
        print ('\n')
    elif CPU == 'carta':
        print('Hai vinto')
        print ('\n')


print('La CPU ha scelto: {}'.format(CPU))
print('Tu hai scelto: {}'.format(user))

