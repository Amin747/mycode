#!/usr/bin/python3
from random import randint


# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Game Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'south' : 'Game Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            },
            'Game Room' : {
                'east'  : 'Hall',
                'item'  : 'knife'
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters Game Room with a montster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and rooms[currentRoom]=='Game Room':
      print('Use the knife in the game room and kill the monster')
      break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break

  if currentRoom == 'Game Room' and 'monster' in rooms[currentRoom]['item']:
      print("Welcome to the Game Room! Let's play a game!")
      print("You have 2 choices. Fight me with a knife or escape. The choice is yours!")
      #.lower() for case-sensitive
      choice = input().lower()

      if choice == 'fight':
          print("So you've decided to be brave and fight me...Alright, let's see what you got")
          fight_power = randint(0, 5) 
          print(f"You're fighting me at level {fight_power}...")
              
          if fight_power >= 4:
              print (f"You are super power with {fight_power} fight power. I can't survive this...")
              print("I'm dead")
              break 
          elif fight_power >= 2 and fight_power <=3:
              print("You might be a monster, but I can stab you with my knife...")
              print("Let's fight till the last breath...")
              
          else: 
              print(f"I have won...The monster is now dead...Good overcame evil")
              
      if choice == 'escape':
          print("So you wanna escape...Let's see if I can catch you")
          playerResponse1 = input("Do you wanna run or fly?\n").lower()
          if playerResponse1 == 'fly':
              print("Monster, you can't freaking fly!!! You're a monster and you're gonna diee...")
          else:
              print("I'm coming to catch you...let's see who runs faster...")
