# Note: No need for comments that don't add any extra explanation, I can understand just by seeing the name & content of the variable
# Note: When re-using the same variables over and over, put them in caps lock 
ACTIONS = ['explore', 'examine', 'unlock door', 'navigate', 'restart', 'quit']
ITEMS = ['couch', 'piano', 'queen bed', 'double bed', 'dresser', "dining table"]
DOORS = ['door A', 'door B', 'door C', 'door D']
KEYS = ['key door A', 'key door B', 'key door C', 'key door D']
AREAS = {
    "game room" : ['couch', 'piano', 'door A', 'key door A'],
    "bedroom 1": ['queen bed', 'door A', 'door B', 'door C', 'key door B'],
    "bedroom 2": ['double bed', 'door B', 'dresser', 'key door D', 'key door C'],
    "living room": ["dining table", 'door C', 'door D'],
    "outside": ["freedom"]
}

STATE = {
    'space_path' : [], # player current space to navigate and make a space path
    'item_path' : [], # to select an item to examine for key; and make an item path
    'inventory': [], # to store found keys
    'time': ["display_clock_countdown"] , #library time for live timer and countdown
}

# Note: All constants should stay at the top
PATHS = {
    'space_path': [],
    'item_path': [],
    'door_path': [],
}

def player_action(player_input: str):
    """can still input another action or repeat same one""" # Moved explanation under function definition
    while player_input != 'quit' and player_input != 'restart': # While player_input is not 'quit' and 'restart'
        print("\Here is a list of actions :",actions) # Print the list of actions
        action = input("PLAYER! Enter your action:").lower() # Player inputs space of choice
        if action in actions:
            return action
        elif action == 'quit': # Exit the function to restart the game
            print("Quitting the game. Goodbye!")
            break
        elif action == 'restart': # Restart the game
            print("Game restarting!")
            player_action('play')
        else:
            print("Value Error, choose again!")
    return action

def explore(space: str):
    """TODO: ADD EXPLANATION HERE"""
    space_items = []
    print(f"You are exploring {space}. You see these items:")
    for item in items:
        print("-", item)
        space_items.append(item)
    return space_items

def examine(space:str):
    """TODO: ADD EXPLANATION HERE"""
    print(f'Here is a list of items in {space}:', explore(space))
    select_item= input(f'Select an item to examine:') #select item
    print((f'You are examining :{select_item}'))
    
    print(f'Examining the {select_item} carefully...')
    for select_item in space:
        # TODO: Check match/case syntax in Python to replace loads of elif statements
        if select_item == 'couch':
            key= ''
            check(space, select_item, key)
        elif select_item == 'piano':
            key= 'key door A'
            check(space, select_item, key)
        elif select_item == 'queen bed':
            key= 'key door B'
            check(space, select_item, key)
        elif select_item == 'double bed':
            key= 'key door C'
            check(space, select_item, key)
        elif select_item == 'dresser':
            key= 'key door D'
            check(space, select_item, key)
        elif select_item == 'dinning table':
            key= ''
            check(space, select_item, key)
        else:
            print("Value ERROR !", examine(space))
        result=check(space, select_item, key)
        return result 

def check(space, select_item, key):
    if ( key!='' and key not in game_state['inventory'] ): 
        print(f'You found {key} in {select_item}')
        update_inventory(key)
        result = True
    elif key=='':
        print(f'No key found in {select_item}')
        result=False
    else: 
        print(f'You already have the key in your inventory {game_state["inventory"]}')  
        result=False
    return result

def unlock_door(action, space, door, inventory: list ):
    # Note: What's happening here?
for i in game_areas:
    
    if 'key door A' in game_state['inventory']:
        unlock()

    print(f'You chose to unlock in {current_space} ')
        if door in space:
        door = input("Enter the door you want to try unlock : ").lower() # Player inputs space of choice
        
        if door in doors:
            print(f'Player chose to try unlock: {door}')

            if key in inventory:
                print(f"This key is already in your inventory !")
                return True
    quiz(door)
    update_door_path(door)
    
    return game_state['door_path']

def quiz(current_door):
    """Quiz function to unlock doors"""
    if (game_state.inventory in current_door):
        print("This door is already unlocked ~ you can proceed!")
        return player_action('play')
    else:
        print("Answer the following question to unlock the door:")
        print("What is 7 + 6?")
        answer = int(input("Your answer: "))
        if answer == 13:
            print("Correct! The door is now unlocked...")
            game_state.inventory.append(current_door)
            return True
        else:
            print("Incorrect answer. Try again!")
            return quiz(current_door)
    return player_action('play')

if door == 'door A':
# Note: What's happening here?    

def quiz('door A'):
    print("Question: What is the primary function of Door A, as suggested by its location in the floor plan?")
    print("A) To access the outdoors.")
    print("B) To provide entry or exit to a specific room.")
    print("C) To serve as a decorative element.")

    answer = input("Enter your choice (A, B, or C): ").upper()

    if answer == "B":
        print("Correct! Door A is most likely for entering or exiting a room.")
    else:
        print("Incorrect. Try again!")

def door_b_quiz():
    print("Question: Considering the layout, which room is Door B most likely connected to?")
    print("A) The Game Room")
    print("B) Bedroom 1")
    print("C) The Outdoors")

    answer = input("Enter your choice (A, B, or C): ").upper()

    if answer == "B":
        print("Correct! Based on the plan, Door B likely leads to Bedroom 1.")
    else:
        print("Incorrect. Try again!")


def door_c_quiz():
    print("Question: If you wake up on the couch, and the key to Door C is found nearby, what is the most logical room Door C leads to, considering the floor plan?")
    print("A) The Game Room")
    print("B) Bedroom 2")
    print("C) The Outdoors")

    answer = input("Enter your choice (A, B, or C): ").upper()

    if answer == "C":
        print("Correct! It makes sense that Door C might lead outside.")
    else:
        print("Incorrect. Consider the layout again!")

def door_d_quiz():
    print("Question: Considering the floor plan, and the fact you woke up on the couch, where is Door D most likely located?")
    print("A) In the Game Room")
    print("B) In Bedroom 1")
    print("C) Not visible on the plan")

    answer = input("Enter your choice (A, B, or C): ").upper()

    if answer == "C":
        print("Correct! Since Door D isn't shown, it's not visible on the plan.")
    else:
        print("Incorrect. Maybe Door D is a secret door?")


print('Player is navigating to a new space!') # Note: This print is outside the function

def navigate(space, door, inventory):
    print(f'Navigating through the {door}')
    if door in game_paths[door_path] and space in spaces:
        while (action == 'unlock door' and action != 'quit' and action != 'restart'):
            # Note: Too many conditionals... I would prefer nested statements here
            if ('door A' in space) and ('door B' not in space) and ('door C' not in space) and ('door D' not in space):
                update_space_path('game room')

            elif ('door A' in space) and ('door B' in space) and ('door C' in space) and ('door D' not in space):
                update_space_path('bedroom 1')
        
            elif ('door A' not in space) and ('door B' in space) and ('door C' not in space) and ('door D' not in space):
                update_space_path('bedroom 2')
        
            elif ('door A' not in space) and ('door B' not in space) and ('door C' in space) and ('door D' in space):
                update_space_path('living room')
        
            elif ('door A' not in space) and ('door B' not in space) and ('door C' not in space) and ('door D' in space):
                update_space_path('outside')
                print("FREEDOM | YOU WIN !")
                print(game_state)
                break
            else:
                ("UNKNOWN SPACE in the system?")
            print(f'You are now in{space}')
        update_space_path(space)



# update space path [game room, bedroom 1, bedroom 2...]
def update_space_path(current_space:str):
    game_paths['space path'].append(current_space)
    return game_paths['space path']

# update item path [couch, piano, queen bed...]
def update_item_path(item:str):
    game_paths['item path'].append(item)
    return game_paths['item path']

# update door path [door A, door B, door C, ...]
def update_door_path(door:str):
    game_paths['door path'].append(door)
    return game_paths['door path']

# update inventory [key door A, key door B, key door C...]
def update_inventory(key:str):
    game_paths['inventory'].append(key)
    return game_paths['inventory']

# display_clock_countdown

################## UPDATE GAME STATE ######################################################
game_state = {
    'space_path': [],
    'item_path': [],
    'door_path': [],
    'inventory': [],
    'time':["display_clock_countdown"]
    }

def update_inventory(key: str, space: str):
    game_state["inventory"].append(key)
    return game_state["inventory"]

def update_game_state(door: str, key: str, item: str, space: str):
    update_space_path(space) #update space
    update_item_path(item) #update item
    update_door_path(door) #update door
    update_inventory(key) #update key
    display_clock_countdown() #run clock countdown

    
################## RESTART FUNCTION ######################################################

def restart(answer: bool):
    reset_game_state()
    
################## PLAYER_INPUT = RESTART ######################################################

def reset_game_state():
    answer = input("Do you want to restart the game? Enter: YES or NO")
    while answer !='YES' and answer!='NO':
        answer = input("To restart Enter only : YES or NO")
    
    if answer.low() == 'yes':
        print("Restarting the game...")
        game_state["space_path"].append('game room')
        game_state["item_path"].clear()
        game_state["inventory"].clear()
        game_state["door_path"].clear()
    elif answer.low() == 'no':
        print("Continue to play...")
        player_action('play')
    else:
        print("Value Error: Enter YES or NO")

    return game_state


################## PLAYER_INPUT = QUIT ######################################################

def quit():
    print("Quitting the game...")
    return game_state



##########################################################################################################
################## EXTRA FEATURES CAN BE ADDED HERE ######################################################
##########################################################################################################

# define Function to display live clock and countdown timer
import time
import sys
from datetime import datetime, timedelta

def display_clock_countdown(minutes):
    try:
        while True:  # Repeat indefinitely (change True to play=true)
            end_time = datetime.now() + timedelta(minutes=minutes)

            while True:
                # Current time
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")

                # Remaining time
                remaining_time = end_time - now
                if remaining_time.total_seconds() <= 0:
                    print(f"\rClock: {current_time} | Countdown: 00:00:00 ⌛", end="")
                    break

                hours, remainder = divmod(int(remaining_time.total_seconds()), 3600)
                mins, secs = divmod(remainder, 60)
                countdown_str = f"{hours:02}:{mins:02}:{secs:02}"

                # Print live clock and countdown on one line
                print(f"\r🕰️ Clock: {current_time} | ⏳ Countdown: {countdown_str}", end="")
                sys.stdout.flush()

                time.sleep(1)

            # Big "Time's Up" banner
            print("\n" + "*"*50)
            print("*****            TIME'S UP!            *****")
            print("*****      Restarting countdown...     *****")
            print("*"*50 + "\n")
            time.sleep(1)  # Optional pause before restarting

    except KeyboardInterrupt:

        print("\nCountdown stopped manually.")
