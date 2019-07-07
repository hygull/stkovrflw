MAP = {'foyer_forward': 'hall',
   'foyer_right': 'bedroom',
   'foyer_back': 'front door',
   'foyer_left': 'office',
   'hall_back': 'foyer',
   'hall_left':'kitchen',
   'bedroom 2_back': 'hall',
   'bedroom_back': 'foyer',
   'bedroom_left': 'bathroom',
   'front door_back': 'foyer',
   'office_back': 'foyer',
   'kitchen_back': 'hall',
   'bathroom_back': 'bedroom'}

def hellokitchen():
    guess = input("your plan works!")
    if guess == 'sup':
        print("YOUR PLAN DEFINITELY WORKS")
    return




DESC = {'foyer': 'You are in the foyer of the house',
    'hall': 'You are in the Hall. The place is completely ruined, and you despise the look of it. ',
    'bedroom': 'You are in the bedroom. The body of the victim is lying on the floor, drenched in blood. A pungent smell is radiating out of the corpse. There are two doors, one back to the foyer, and one leading to the bathroom on the left.',
    'front door': 'The front door is locked. You have to find the murderer to escape! Type back to return to the foyer.',
    'office': 'You walk into a room which looks like an Office. You scour the room for evidence but return nothing. Type back to return to the foyer.',
    'kitchen': hellokitchen(),
    'bathroom': 'You are in the bathroom'}


FINISH = 'SECRET_ROOM'
UNLOCKED_DOOR = 'kitchen'

name = input('\033[1;36;1m What is your name? > ')
print('Hello', name)
print("ENTER STARTING DESC.")

room = 'foyer'

while True:
    print(DESC[room])
    if room in FINISH:
        break

direction = input('Enter a direction. Choose from forward, back, left, right or quit >')
key = room + '_' + direction

if key in MAP:
    room = MAP[key]

else:
    print('You can\'t go ' + direction + '.')

print('Congratulations!')