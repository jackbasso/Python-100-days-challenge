import random

human_selection = int(input("What do you choose? 0 for rock, 1 for paper and 2 for scissor  "))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
selection = [rock, paper, scissors]
print("Your selection is:")
print(selection[human_selection])

pc_selection = random.randint(0,2)
print("Computer selection is:")
print(selection[pc_selection])

if human_selection == pc_selection:
  print("PLAY AGAIN, IS A TIE")
elif human_selection == 0 and pc_selection == 2:
  print("YOU WON")
elif human_selection == 1 and pc_selection == 0:
  print("YOU WON") 
elif human_selection == 2 and pc_selection == 1:
  print("YOU WON")
else:
  print("YOU LOST")