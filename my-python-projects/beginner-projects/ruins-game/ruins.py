rounds = ["You wake up inside ancient ruins. The air is damp and cold. "
          "There are two exits.",
          "The tunnel leads to a narrow bridge over a deep pit. The bridge"
          " looks unstable.", 
          "On the other side, you find a room with a glowing symbol on the"
          " floor and a stone lever.", 
          "A hallway splits into two paths. One smells of fresh air,"
          " the other smells of smoke.", 
          "You reach a locked gate. A keypad beside it shows worn buttons.",
          "Beyond the gate is a ladder leading up and a dark tunnel "
          "leading down."]

options = ['A: Enter the dark tunnel', 'B: Open the rusty metal door',
           'A: Run across the bridge', 'B: Walk slowly and carefully',
           'A: Step on the glowing symbol', 'B: Pull the stone lever',
           'A: Follow the smell of smoke', 'B: Follow the fresh air',
           'A: Press the most worn buttons', 'B: Press random buttons',
           'A: Climb the ladder', 'B: Enter the dark tunnel']

deaths = ['The door collapses and crushes you. You lose!',
          'The bridge snaps under your weight. You lose!',
          'The symbol triggers a deadly trap. You lose!',
          'The smoke comes from a fire trap. You lose!',
          'The gate releases poison gas. You lose!',
          'You get mauled by a bear in the tunnel You lose!']

print("Welcome to Escape the Ruins v1\n")
input("Press Enter to Start\n\n\n")

# Round 1
print("\n\n\n\n\n"
      f"{rounds[0]}\n")
answer = input(f"{options[0]}\n{options[1]}\n\n"
               "Choose your path: ")
if answer == 'A' or answer == 'a':
    pass
elif answer == 'B' or answer == 'b':
    print(f'\n\n\n{deaths[0]}')
    quit()
else:
    print('\n\n\nPlease choose either A or B')
    quit()
    
# Round 2    
print("\n\n\n\n\n"
      f"{rounds[1]}\n")
answer = input(f"{options[2]}\n{options[3]}\n\n"
               "Choose your path: ")
if answer == 'A' or answer == 'a':
    print(f'\n\n\n{deaths[1]}')
    quit()
elif answer == 'B' or answer == 'b':
    pass
else:
    print('\n\n\nPlease choose either A or B')
    quit()
    
# Round 3
print("\n\n\n\n\n"
      f"{rounds[2]}\n")
answer = input(f"{options[4]}\n{options[5]}\n\n"
               "Choose your path: ")
if answer == 'A' or answer == 'a':
    print(f'\n\n\n{deaths[2]}')
    quit()
elif answer == 'B' or answer == 'b':
    pass
else:
    print('\n\n\nPlease choose either A or B')
    quit()
    
# Round 4
print("\n\n\n\n\n"
      f"{rounds[3]}\n")
answer = input(f"{options[6]}\n{options[7]}\n\n"
               "Choose your path: ")
if answer == 'A' or answer == 'a':
    print(f'\n\n\n{deaths[3]}')
    quit()
elif answer == 'B' or answer == 'b':
    pass
else:
    print('\n\n\nPlease choose either A or B')
    quit()
    
# Round 5
print("\n\n\n\n\n"
      f"{rounds[4]}\n")
answer = input(f"{options[8]}\n{options[9]}\n\n"
               "Choose your path: ")
if answer == 'A' or answer == 'a':
    pass
elif answer == 'B' or answer == 'b':
    print(f'\n\n\n{deaths[4]}')
    quit()
else:
    print('\n\n\nPlease choose either A or B')
    quit()
    
# Round 6
print("\n\n\n\n\n"
      f"{rounds[5]}\n")
answer = input(f"{options[10]}\n{options[11]}\n\n"
               "Choose your path: ")
if answer == 'A' or answer == 'a':
    print("YOU WON! CONGRATS!")
    input("\n\nThanks for playing.\n")
elif answer == 'B' or answer == 'b':
    print(f'\n\n\n{deaths[5]}')
    quit()
else:
    print('\n\n\nPlease choose either A or B')
    quit()